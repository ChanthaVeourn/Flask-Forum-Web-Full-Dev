from flask import render_template, redirect, url_for, Blueprint, flash, request, make_response

from app.models.Tag import TagModel
from app.database import session
from flask_login import login_required, login_user, logout_user

tag_blueprint = Blueprint('tag', __name__, template_folder="app/templates/", url_prefix="/tag")


@tag_blueprint.route("/create-tag/", methods=['GET'])
def create_tag():

    tag1 = TagModel({'name':"Python", 'description':"Anything related to python programming."})
    tag2 = TagModel({'name':"Java", 'description':"Anything related to Java programming."})
    tag3 = TagModel({'name':"Web Development", 'description':"Anything related to Web developmnet."})
    tag4 = TagModel({'name':"Mobile App Development", 'description':"Anything related to App development."})

    session.add(tag1)
    session.add(tag2)
    session.add(tag3)
    session.add(tag4)
    session.commit()

    return make_response("Tag has been created.",200)


