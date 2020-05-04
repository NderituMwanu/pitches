from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_mail import Mail


# from .config import DevConfig
mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    mail.init_app(app)


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)#initializing our application

    manager = Manager(app)

    #initializing flask extension
    bootstrap = Bootstrap(app)

    #setting up configuration
    app.config['SECRET_CODE'] = '12345'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://ms:New Password@localhost/USER'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    #user loading
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

# from app import views