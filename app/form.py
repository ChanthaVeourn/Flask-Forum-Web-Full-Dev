from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, validators, BooleanField, TextAreaField


class RegisterForm(FlaskForm):
    
    username = StringField('Username', 
        validators=[validators.Length(min=5, max=30)])

    email_address = StringField("Email Address" ,
        validators=[validators.Length(max=120)])

    password1 = PasswordField('New Password', 
        validators=[
        validators.DataRequired(),
        validators.EqualTo("password2",
        message='Passwords must match')
        ])

    password2 = PasswordField("Confirm Password", validators=[validators.DataRequired()])

    accept_tos = BooleanField('I accept the terms and conditions.', validators=[validators.DataRequired()])

    create = SubmitField("Create Account")

class LoginForm(FlaskForm):
    
    email_address = StringField("Email Address" ,[
        validators.DataRequired(),
        validators.Length(max=120)])

    password = PasswordField('New Password', validators=[validators.DataRequired()])
    
    sign_in = SubmitField(label="Sign in")


class CreateForumForm(FlaskForm):
    title = StringField("Forum topic", validators=[validators.DataRequired(),validators.Length(max=120)])
    description = TextAreaField(validators=[ validators.DataRequired(), validators.Length(max=1000)])
    
    create = SubmitField("Create Forum")

class UpdateForumForm(FlaskForm):
    title = StringField("Forum topic", validators=[validators.DataRequired(),validators.Length(max=120)])
    description = TextAreaField(validators=[ validators.DataRequired(), validators.Length(max=1000)])
    
    update = SubmitField("Update Forum")

class ReplyForm(FlaskForm):
    title = StringField('title', [validators.Length(min=4, max=64)])
    description = StringField('description', [validators.Length(min=4)])