import os
from flask import (Flask, flash, render_template, redirect,
                   request, url_for, session)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# For security features used in registwer and login pages
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_paginate import Pagination, get_page_args
# Only import env if env.py path exists
if os.path.exists("env.py"):
    import env

# Create instance of Flask
app = Flask(__name__)


# Adding
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Create an instance of pymongo
mongo = PyMongo(app)


def pag_items(items):
    """
    Uses flask_pagination and list methods to display 9 items per page
    sorted by the most recently added item.
    ***Page pagination code was modified from mozillazg GitHub demo and
    Pretty Printed Youtube Tutorial on Query Pagination in Flask and MongoDB***
    """
    # getting page arguments for pagination
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    # set limit of 9 items per page
    limit = 9
    # calc offset of items for each page
    offset = page * limit - limit
    total = len(items)
    # selecting items for each page
    return items[offset: offset + limit]


def pagination_arg(items):
    # getting page arguments for pagination
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    # Total of all items in items list
    total = len(items)
    # Setting pagination parameters
    return Pagination(page=page, per_page=9, total=total,
                      css_framework="bootstrap3")


@app.route("/")
@app.route("/home")
def home():
    """
    Display home page with top 3 liked items
    """
    items = mongo.db.items.find().sort("liked_count", -1).limit(3)
    all_users = list(mongo.db.users.find())
    if session:
        user_liked_by = mongo.db.matches.find_one({"username": session['user']})["liked_by"]
        user_data = mongo.db.users.find_one({"username": session['user']})
        return render_template("index.html", items=items, all_users=all_users, user=user_data, liked=user_liked_by)

    return render_template("index.html", items=items, all_users=all_users)


@app.route("/items", methods=["GET", "POST"])
def items():
    """
    Display all items sorted by the most recent added
    and Paginate displayed items

    If a user is logged in, retrieve a list of usernmaes they 
    are liked by and retrieve user data to be used in matching
    """
    items = list(mongo.db.items.find().sort('_id', -1))
    # Retrieve Pagination parameters
    items_paginated = pag_items(items)
    pagination = pagination_arg(items)

    categories = mongo.db.categories.find()

    all_users = list(mongo.db.users.find())
    
    if session:
        user_liked_by = mongo.db.matches.find_one({"username": session["user"]})["liked_by"]
        user_data = mongo.db.users.find_one({"username": session["user"]})
        return render_template("items.html", items=items_paginated,
                            categories=categories, pagination=pagination,
                            liked=user_liked_by, user=user_data, all_users=all_users)
                            
    return render_template("items.html", items=items_paginated,
                           categories=categories, pagination=pagination, all_users=all_users)



@app.route("/filter")
def filter():
    """
    Get all checked values for category filter,
    find and display items with those categories
    """
    categories = mongo.db.categories.find()
    selected_categories = request.args.getlist("selected-categories")
    items = list(mongo.db.items.find(
        {"category": {"$in": selected_categories}}).sort('_id', -1))

    items_paginated = pag_items(items)
    pagination = pagination_arg(items)

    if session:
        user_data = mongo.db.users.find_one({"username": session["user"]})
        user_liked_by = mongo.db.matches.find_one({"username": session["user"]})["liked_by"]
        return render_template("items.html", items=items_paginated,
                            categories=categories,
                            selected_categories=selected_categories,
                            pagination=pagination,
                            liked=user_liked_by, user=user_data)

    return render_template("items.html", items=items_paginated,
                           categories=categories,
                           selected_categories=selected_categories,
                           pagination=pagination)


@app.route("/sort/<sort_by>")
def sort(sort_by):
    """
    Sort items alphabetically, reverse alphabetically,
    by the latest date added, by liked items or
    by item being flagged
    """
    categories = mongo.db.categories.find()
    if sort_by == 'a-to-z':
        items = list(mongo.db.items.find().sort("item_name", 1))
    elif sort_by == 'z-to-a':
        items = list(mongo.db.items.find().sort("item_name", -1))
    elif sort_by == 'date':
        items = list(mongo.db.items.find().sort("created_on", -1))
    elif sort_by == 'liked':
        items = list(mongo.db.items.find({"liked_by": session['user']}))
    elif sort_by == 'flagged':
        items = list(mongo.db.items.find().sort("flagged", -1))

    items_paginated = pag_items(items)
    pagination = pagination_arg(items)

    if session:
        user_liked_by = mongo.db.matches.find_one({"username": session["user"]})["liked_by"]
        user_data = mongo.db.users.find_one({"username": session["user"]})
        return render_template("items.html", items=items_paginated,
                            categories=categories, pagination=pagination,
                            liked=user_liked_by, user=user_data)
    
    return render_template("items.html", items=items_paginated,
                        categories=categories, pagination=pagination)


@app.route("/search")
def search():
    """
    Use an index from items collections to allow the user
    to search through the item names and item short description
    """
    categories = mongo.db.categories.find()
    query = request.args.get("search")

    items = list(mongo.db.items.find({"$text": {"$search": query}}))
    
    items_paginated = pag_items(items)
    pagination = pagination_arg(items)

    if session:
        user_liked_by = mongo.db.matches.find_one({"username": session["user"]})["liked_by"]
        user_data = mongo.db.users.find_one({"username": session["user"]})
        return render_template("items.html", items=items_paginated,
                                categories=categories, pagination=pagination,
                                liked=user_liked_by, user=user_data, query=query)

    return render_template("items.html", items=items_paginated,
                           categories=categories, pagination=pagination, query=query)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Checks if a username already exists, if not, the
    usernme and password is added to the users database,
    otherwise the user is redirected to the registration page
    """
    categories = mongo.db.categories.find()
    if request.method == 'POST':
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})
        if existing_user:
            flash("A Swapper already has this name, pick a new one!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get("password")),
            "user_image": request.form.get("user-img"),
            "looking_for": request.form.getlist("looking_for"),
            "fb_msgr": request.form.get("fb-msgr"),
            "whatsapp": request.form.get("whatsapp"),
            "instagram": request.form.get("instagram")
        }

        mongo.db.users.insert_one(register)

        # Add new user to matches database to facilitate
        mongo.db.matches.insert_one(
            { "username": request.form.get("username"),
            "liked_by": [],
            "matched_items": [],
            "matched_creator": []})

        session["user"] = request.form.get("username")
        flash("You're officially a Swapper now, woo!")
        return redirect(url_for('items', username=session['user']))

    return render_template("register.html", categories=categories)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Checks if username exists in the database and if it does,
    return the username. The unhashed password from this user's
    dictionary is chekced against the entered password. If password
    or username don't match then a flash message is provided to user as
    feedback.
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})
        # checks if the hashed password in DB matches entered one
        if existing_user:
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username")
                flash("Welcome Back {}".format(session["user"]))
                return redirect(url_for('my_profile', username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for('login'))
        # If user doesn't exist
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route('/logout')
def logout():
    """
    Implement log out functionality by removing user from
    the session cookie
    """
    flash("See you soon")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_item", methods=["GET","POST"])
def add_item():
    """
    Insert new items added into Items collection along with
    date and time when item was created and the user who
    created the item
    """
    categories = mongo.db.categories.find()
    if request.method == "POST":
        new_item = {
            "item_image": request.form.get("item_image"),
            "item_name": request.form.get("item_name"),
            "short_description": request.form.get("short_desc"),
            "long_description": request.form.get("long_desc"),
            "category": request.form.get("category"),
            "size_gender": request.form.get("item_fit"),
            "size_country": request.form.get("size_region"),
            "size": request.form.get("size"),
            "used_status": request.form.get("used_status"),
            "created_on": datetime.now(),
            "created_by": session["user"],
            "liked_by": [],
            "liked_count": 0,
            "flagged": "N",
        }
        mongo.db.items.insert_one(new_item)
        flash("Item added succesfully")
        return redirect(url_for('items', username=session['user']))

    user_data = mongo.db.users.find_one({"username": session["user"]})
    return render_template("add_item.html", categories=categories, user=user_data)


@app.route("/edit_item/<item_id>", methods=["GET", "POST"])
def edit_item(item_id):
    """
    Edit a chosen item identified by item_id and display updated version
    after changes have been submitted
    """
    if request.method == "POST":
        edited_item = {
            "item_image": request.form.get("item_image"),
            "item_name": request.form.get("item_name"),
            "short_description": request.form.get("short_desc"),
            "long_description": request.form.get("long_desc"),
            "category": request.form.get("category"),
            "size_gender": request.form.get("item_fit"),
            "size_country": request.form.get("size_region"),
            "size": request.form.get("size"),
            "used_status": request.form.get("used_status"),
            "created_on": datetime.now(),
            "created_by": session["user"],
            "liked_by": [],
            "liked_count": 0,
            "flagged": "N",
        }
        mongo.db.items.update({"_id": ObjectId(item_id)}, edited_item)
        flash("'{}' updated succesfully".format(edited_item["item_name"]))
        return redirect(url_for('items', username=session['user']))

    item = mongo.db.items.find_one({"_id": ObjectId(item_id)})
    categories = mongo.db.categories.find()
    user_data = mongo.db.users.find_one({"username": session["user"]})
    return render_template("add_item.html", categories=categories, item=item, user=user_data)



@app.route('/delete_item/<item_id>')
def delete_item(item_id):
    # Delete selected item
    mongo.db.items.remove({'_id': ObjectId(item_id)})
    return redirect(url_for('items', username=session['user']))

 
@app.route('/liked_item/<item_id>/<action>')
def liked_item(item_id, action):
    """
    If user likes an item, add them to the items collection,
    liked_by array. If the user unlikes the item,
    remove them from the same array
    """
    user = session['user']
    user_liked_by = mongo.db.matches.find_one({"username": user})["liked_by"]
    item_creator = mongo.db.items.find_one(
        {"_id": ObjectId(item_id)})["created_by"]
    item_creator_liked_by = mongo.db.matches.find_one(
        {"username": item_creator})["liked_by"]
    # Add user to liked_by array in the item dictinory and increase like count
    if action == 'like':
        mongo.db.items.update_one({"_id": ObjectId(item_id)},
                                  {'$push': {'liked_by': user}, '$inc': {'liked_count': 1}})
        # Add user to creators liked_by array
        if user not in item_creator_liked_by:
            mongo.db.matches.update_one({"username": item_creator},
                                        {'$push': {'liked_by': user}})
        # Check if item creator has liked users items and match them
        if item_creator in user_liked_by:
            flash("""It's a match! You can now click
                  on {}'s username and say hi :)""".format(item_creator))

    # Remove user from liked_by array in item dictionary
    elif action == 'unlike':
        mongo.db.items.update_one({"_id": ObjectId(item_id)},
                                  {'$pull': {'liked_by': user}, '$inc': {'liked_count': -1}})
        # check if user likes any other creator items
        all_items_from_creator = list(mongo.db.items.find({"created_by": item_creator}))
        liked_items_from_creator = []
        for item in all_items_from_creator:
            # Add all liked items by the same creator in a list
            if user in item["liked_by"]:
                liked_items_from_creator.append(item["item_name"])

            # If list=0 remove user from creators matched dictionary 
        if len(liked_items_from_creator) == 0:
            mongo.db.matches.update_one({"username": item_creator},
                        {'$pull': {'liked_by': user}})
     
    return redirect(request.referrer)


@app.route('/flagged_item/<item_id>/<action>')
def flagged_item(item_id, action):
    """
    Allows users to flag items and admin to unflag
    """
    if action == 'flag':
        mongo.db.items.update_one({"_id": ObjectId(item_id)}, {'$set': {'flagged': 'Y'}})
    
    elif action == 'unflag':
        mongo.db.items.update_one({"_id": ObjectId(item_id)}, {'$set': {'flagged': 'N'}})
    
    return redirect(request.referrer)


@app.route('/my_profile/<username>')
def my_profile(username):
    """
    Get session user data and items data,
    Display them on user's profile page
    """
    items = list(mongo.db.items.find())
    item_count = mongo.db.items.find({"created_by": username}).count()
    all_users = list(mongo.db.users.find())
    user_liked_by = mongo.db.matches.find_one({"username": username})["liked_by"]
    user_data = mongo.db.users.find_one({"username": username})
    matches = list(mongo.db.items.find(
        {"created_by": {"$in": user_liked_by}, "liked_by": session['user']}))
    
    return render_template('my_profile.html', items=items, user=user_data, item_count=item_count, liked=user_liked_by, matches=matches, all_users=all_users)


@app.route('/edit_profile/<username>', methods=['GET', 'POST'])
def edit_profile(username):
    """
    Edit user's profile
    """
    categories = mongo.db.categories.find()
    user_data = mongo.db.users.find_one({"username": username})

    if request.method == 'POST':
        edited_profile = {
            "username": user_data["username"],
            "password": user_data["password"],
            "user_image": request.form.get("user-img"),
            "looking_for": request.form.getlist("looking-for"),
            "fb_msgr": request.form.get("fb-msgr"),
            "whatsapp": request.form.get("whatsapp"),
            "instagram": request.form.get("instagram")
        }

        mongo.db.users.update({"username": session['user']}, edited_profile)
        flash("{}'s profile updated succesfully".format(edited_profile["username"]))
        return redirect(url_for('my_profile', username=username))

    return render_template("edit_profile.html", categories=categories, user=user_data )


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
