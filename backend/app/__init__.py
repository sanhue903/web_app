from flask import Flask
from flask_cors import CORS
from config import Config

from app.extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    db.init_app(app)
    create_database()

    # Register blueprints here


    return app

def create_database():
    from app.models.user import User
    from app.models.student import Student
    from app.models.aule import Aule
    
    db.create_all() 