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
    app.register_blueprint(student_bp, url_prefix='/apps/<mobile_app_id>')
    
    from app.score import bp as score_bp
    app.register_blueprint(score_bp, url_prefix='/apps/<mobile_app_id>/aules/<aule_id>')

    return app

def create_database():
    from app.models import User, Student, Aule, School, MobileApp, Chapter, Question, Score
    
    db.create_all() 
    
def initial_data():
    from app.models import MobileApp, Chapter, Question

    mobile_app = MobileApp('BOTIKI', 'El Botiquin de las Emociones')
    db.session.add(mobile_app)
    db.session.commit()

    chapter_1 = Chapter('CONEMO', 'Conciencia Emocional', mobile_app.id)
    db.session.add(chapter_1)
    db.session.commit()
    
    question_1 = Question('CETRIS', 'pregunta sobre la tristeza', chapter_1.id)
    db.session.add(question_1)
    db.session.commit()