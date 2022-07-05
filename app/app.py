from flask import Flask, Blueprint
from flask_login import LoginManager
from app.routes import *
from app.models import User

app = Flask(__name__)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(user_id)
   
all_route = [route for name, route in globals().items() if isinstance(route , Blueprint)]

for route in all_route:
    app.register_blueprint(route)

def create_app(app=None,config=None):
    if config:
        app.config.from_object(config)
    login_manager.init_app(app)
    return app


    

