from flask import render_template, redirect, url_for, Blueprint


views = Blueprint('views', __name__, template_folder="app/templates/")


@views.route("/home/")
@views.route("/")
def home():
    return render_template("index.html")



