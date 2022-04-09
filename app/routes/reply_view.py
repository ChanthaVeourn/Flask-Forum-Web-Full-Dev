from flask import render_template, redirect, url_for, Blueprint, request, abort, flash
from app.models import *

from flask_login import current_user, login_required

from app.form import ReplyForm
reply_blueprint = Blueprint('reply', __name__,template_folder="app/templates/",url_prefix="/reply")

@reply_blueprint.route('/<slush>/', methods=['GET', 'POST'])
def create_reply(slush):

    if request.method == 'POST':
        pass

    current_forum = Forum.query.filter(Forum.slush == slush).one()
    if not current_forum:
        abort(404)
    
    #all_replies = current_forum

    return render_template("all_replies.html", replies = all_replies)


