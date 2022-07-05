from flask import render_template, redirect, url_for, Blueprint, flash, request, make_response

from flask_login import login_required, login_user, logout_user

from app.models import *
from app.form import RegisterForm, LoginForm
from app.database import session       
from flask_bcrypt import check_password_hash


auth = Blueprint('auth', __name__, template_folder="app/templates/", url_prefix="/auth")

@auth.route('/register/', methods=['GET', 'POST'])
def register():
    
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        if form.password1.data == form.password2.data:
            new_user = User({ 
                "name" : form.username.data, 
                "email" : form.email_address.data,
                "password" : form.password1.data
                })
            session.add(new_user)
            session.commit()
            login_user(new_user)
            
            flash("Thanks for registering")
            
            return redirect(url_for('views.home'))
        flash("Password not match!")    

    return render_template('register.html', form = form)
    
@auth.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    
    if request.method == "POST" and form.validate():
        user = User.query.filter(User.email == form.email_address.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash(f"Welcome {user.name}", category='success')
                return redirect(url_for('views.home'))
            flash("Incorrect email or password. Please try again.", category='danger')    
        else:
            flash("Incorrect email or password. Please try again.", category='danger')
            
    return render_template('login.html',form=form)   

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out", category='info')
    return redirect(url_for('views.home'))
