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
    items = mongo.db.items.find()
    # Add guest as a session user before user logs in
    if not session['user']:
        session["user"] = "guest"

    items = mongo.db.items.find()

    return render_template("index.html", items=items)


@app.route("/items/<username>", methods=["GET", "POST"])
def items(username):
    """
    Display all items sorted  by the most recent and
    Paginate displayed items
    """
    items = list(mongo.db.items.find().sort('_id', -1))

    items_paginated = pag_items(items)
    pagination = pagination_arg(items)

    categories = mongo.db.categories.find()
    # If user is logged in, add useers data to identify matched and like items
    if username != "guest":
        user_liked_by = mongo.db.matches.find_one({"username": username})["liked_by"]
        user_data = mongo.db.users.find_one({"username": username})
        return render_template("items.html", items=items_paginated,
                            categories=categories, pagination=pagination,
                            liked=user_liked_by, user=user_data)
                            
    return render_template("items.html", items=items_paginated,
                           categories=categories, pagination=pagination)



@app.route("/filter/<username>", methods=["GET", "POST"])
def filter(username):
    """
    Get all checked values for category filter,
    find and display items with those categories
    """
    categories = mongo.db.categories.find()
    selected_categories = request.form.getlist("selected-categories")
    items = list(mongo.db.items.find(
        {"category": {"$in": selected_categories}}).sort('_id', -1))

    items_paginated = pag_items(items)
    pagination = pagination_arg(items)

    if username != "guest":
        user_data = mongo.db.users.find_one({"username": username})
        # a list of users who have liked session user
        user_liked_by = mongo.db.matches.find_one({"username": username})["liked_by"]
        return render_template("items.html", items=items_paginated,
                            categories=categories,
                            selected_categories=selected_categories,
                            pagination=pagination,
                            liked=user_liked_by, user=user_data)

    return render_template("items.html", items=items_paginated,
                           categories=categories,
                           selected_categories=selected_categories,
                           pagination=pagination)


@app.route("/sort/<sort_by>/<username>")
def sort(sort_by, username):
    """
    Sort items alphabetically, reverse alphabetically,
    by the lates date added, by liked items or
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
        items = list(mongo.db.items.find().sort("liked_by", 1))
    elif sort_by == 'flagged':
        items = list(mongo.db.items.find().sort("flagged", -1))

    items_paginated = pag_items(items)
    pagination = pagination_arg(items)

    if username != "guest":
        user_liked_by = mongo.db.matches.find_one({"username": username})["liked_by"]
        user_data = mongo.db.users.find_one({"username": username})
        return render_template("items.html", items=items_paginated,
                            categories=categories, pagination=pagination,
                            liked=user_liked_by, user=user_data)
    
    return render_template("items.html", items=items_paginated,
                        categories=categories, pagination=pagination)


@app.route("/search/<username>", methods=["GET", "POST"])
def search(username):
    """
    Use an index from items collections to allow the user
    to search through the item names and item short description

    If a user likes a searched item, the page is refreshed without 
    a search query being passed in and the page breaks. As a fix, 
    users liked items are being displayed
    """
    categories = mongo.db.categories.find()
    query = request.form.get("search")

    if query == None:
        items = list(mongo.db.items.find({"liked_by": session['user']}))
    else:
        items = list(mongo.db.items.find({"$text": {"$search": query}}))
        

    items_paginated = pag_items(items)
    pagination = pagination_arg(items)

    if username != 'guest':
        user_liked_by = mongo.db.matches.find_one({"username": username})["liked_by"]
        user_data = mongo.db.users.find_one({"username": username})
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
            "looking_for": request.form.getlist("looking_for")
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
                return redirect(url_for('items', username=session["user"]))
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
    return redirect(url_for('login'))


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

    return render_template("add_item.html", categories=categories)


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

    item = mongo.db.items.find_one({"_id": ObjectId(item_id)})
    categories = mongo.db.categories.find()
    return render_template("edit_item.html", categories=categories, item=item)


@app.route('/delete_item/<item_id>')
def delete_item(item_id):
    # Delete selected item
    mongo.db.items.remove({'_id': ObjectId(item_id)})
    flash("Item has been deleted, bye!")
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
    print(request.referrer)       
    return redirect(request.referrer)


@app.route('/my_profile')
def my_profile():
    """
    Get session user data and items data
    """
    items = list(mongo.db.items.find())
    item_count = mongo.db.items.find({"created_by": session["user"]}).count()
    user_liked_by = mongo.db.matches.find_one({"username": session["user"]})["liked_by"]
    user = mongo.db.users.find_one({"username": session["user"]})

    return render_template('my_profile.html', items=items, user=user, item_count=item_count, liked=user_liked_by)


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
