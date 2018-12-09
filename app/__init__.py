import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app.helpers import MyHomeView

#Instantiate Extension Objects
db = SQLAlchemy()
bootstrap = Bootstrap()
admin = Admin(index_view=MyHomeView())
app_bcrypt = Bcrypt()
login_manager = LoginManager()

#Initialize extensions that take app.
def initialize_extensions(app):
    db.init_app(app)
    bootstrap.init_app(app)
    admin.init_app(app)
    app_bcrypt.init_app(app)
    login_manager.init_app(app)

#Register Python packages / Flask blueprints.
def register_blueprints(app):
    from app.auth import authentication as at
    app.register_blueprint(at)
    from app.bins import bins
    app.register_blueprint(bins)

#Pass models that are accessible through /admin route.
def model_to_admin():
    from app.auth.models import User
    admin.add_view(ModelView(User, db.session))

#Application factory method used to create, congfigure and return instance of the application.    
def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)
    initialize_extensions(app)
    register_blueprints(app)
    model_to_admin()
    return app