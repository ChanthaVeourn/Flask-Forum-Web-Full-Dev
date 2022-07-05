from flask import render_template, redirect, url_for, Blueprint, request, abort, flash, make_response
from app.models import *
from app.form import CreateForumForm, UpdateForumForm
from app.database import session

from flask_login import login_required, current_user

from app.form import ReplyForm
forum_blueprint = Blueprint('forum_blueprint', __name__, template_folder="app/templates/",url_prefix="/forum")

@forum_blueprint.route("/")
def all_forum():
    
    forums = Forum.query.all()
    return render_template("forum.html" ,forums = forums)

@forum_blueprint.route("/new-forum/", methods=['GET', 'POST'])
@login_required
def create_forum():
    form = CreateForumForm(request.form)
    
    if request.method == 'POST' and form.validate():
        new_forum = Forum({'title':form.title.data, 'description' : form.description.data,'owner_id' :  current_user._get_current_object().id})
        session.add(new_forum)
        session.commit()
        return redirect(url_for('views.home'))
    tags = TagModel.query.all()
    #return render_template("forum_create.html", form = form, tags = tags)
    response = make_response(render_template("forum_create.html",  form = form, tags = tags))
    return response

@forum_blueprint.route("/created-forum/")
@login_required
def user_forum():
    user = current_user._get_current_object()
    forums = user.forums
    return render_template('created_forum.html',forums = forums)

@forum_blueprint.route("/<slush>/", methods=['GET','POST'])
def single_forum(slush):
    form = ReplyForm(request.form)
    forum = Forum.query.filter(Forum.slush == slush).one()

    user_authentication()

    if request.method == 'POST' and form.validate():
        form_dict = request.form.to_dict()
        new_reply = Reply({'parent_id': current_user._get_current_object().id,'forum_id':forum.id})
        if form_dict:
            for key, value in form_dict.items():
                if hasattr(new_reply, key) and getattr(new_reply, key) != value:
                    setattr(new_reply, key, value)
            session.add(new_reply)
            session.commit()
            flash(f"Created new reply", category='success');

    if not forum:
      abort(404)
    return render_template("single_forum.html", forum = forum, form = form)

@forum_blueprint.route("/update-forum/<id>/",methods=["POST", "GET"])
@login_required
def update_user_forum(id):

    form = UpdateForumForm(request.form)
    forum = Forum.query.get(id)

    if form.validate_on_submit():
        forum.title = form.title.data
        forum.description = form.description.data
        session.commit()
        return redirect(url_for("forum_blueprint.user_forum"))

    return render_template("update_forum.html", form = form, forum = forum)

@forum_blueprint.route("/created-forum/delete/<id>/", methods=["GET"])
@login_required
def delete_forum(id):
    
    forum = Forum.query.filter(Forum.id == id).delete()
    session.commit()
    flash("One forum have been deleted.", category="success")
    return redirect(url_for("forum_blueprint.user_forum"))


def user_authentication():
    if request.method == 'POST' and current_user.is_anonymous:
        flash("Please login to continue.", category='info')
        return redirect(url_for('auth.login'))