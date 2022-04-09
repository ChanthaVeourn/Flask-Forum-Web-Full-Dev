from flask_wtf.csrf import CSRFProtect

from app import create_app, app,DevelopmentConfig

current_app = create_app(app,DevelopmentConfig)
cfrf = CSRFProtect()

if __name__ == "__main__":
    
    cfrf.init_app(app)
    current_app.run()