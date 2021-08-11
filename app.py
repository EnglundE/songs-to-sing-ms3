
# Credit to Code Institute course content for Flask/MongoDB project setup
import os
from s3_functions import show_image
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
BUCKET = "erikms3"

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_categories")
def get_categories():
    contents = show_image(BUCKET)
    lyrics = mongo.db.lyrics.find()
    return render_template("categories.html", lyrics=lyrics, contents=contents)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# ---------------
