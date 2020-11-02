import os
from flask import (Flask, render_template, redirect, request, url_for, session)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# For security features used in registwer and login pages
from werkzeug.security import generate_password_hash, check_password_hash
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


@app.route("/")
@app.route("/home")
def home():
    items = mongo.db.items.find()
    return render_template("index.html", items=items)


@app.route("/items")
def items():
    categories = mongo.db.categories.find()
    items = list(mongo.db.items.find())
    return render_template("items.html", items=items, categories=categories)


@app.route("/filter", methods=["GET", "POST"])
def filter():
    """
    Get all checked values for category filter,
    find and display items with those categories
    """
    categories = mongo.db.categories.find()
    selected_categories = request.form.getlist("selected-categories")
    items = list(mongo.db.items.find(
        {"category": {"$in": selected_categories}}))
    return render_template("items.html", items=items, categories=categories,
                           selected_categories=selected_categories)


@app.route("/sort/<sort_by>")
def sort(sort_by):
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
        items = list(mongo.db.items.find().sort("created_on", 1))
    elif sort_by == 'liked':
        items = list(mongo.db.items.find().sort("liked_by", 1))
    elif sort_by == 'flagged':
        items = list(mongo.db.items.find().sort("flagged", -1))

    return render_template("items.html", items=items, categories=categories)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Use an index from items collections to allow the user
    to search through the itesm names and item shor description
    """
    categories = mongo.db.categories.find()
    query = request.form.get("search")
    items = list(mongo.db.items.find({"$text": {"$search": query}}))
    return render_template("items.html", items=items, categories=categories)


@app.route("/register", methods=["GET", "POST"])
def register():
    categories = mongo.db.categories.find()
    if request.method == 'POST':
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": request.form.get("password"),
            "looking_for": request.form.getlist("looking_for")
        }

        mongo.db.users.insert_one(register)

    return render_template("register.html", categories=categories)

if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
