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
    
    from app.score import bp as score_bp
    app.register_blueprint(score_bp)


    return app

def create_database():
    from app.models.user import User
    from app.models.student import Student
    from app.models.aule import Aule
    from app.models.school import School
    from backend.app.models.mobile.mobile_app import MobileApp
    from app.models.mobile.chapter import Chapter
    from app.models.mobile.question import Question
    from app.models.mobile.score import Score
    
    db.create_all() 