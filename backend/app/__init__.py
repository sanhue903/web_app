from flask import Flask
from flask_cors import CORS
from config import Config

from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    db.init_app(app)
    
    with app.app_context():
        create_database()

    # Register blueprints here
    
    from app.student import bp as student_bp
    app.register_blueprint(student_bp, url_prefix='/students')


    return app

def create_database():
    from app.models.user import User
    from app.models.student import Student
    from app.models.aule import Aule
    from app.models.school import School
    
    db.create_all() 