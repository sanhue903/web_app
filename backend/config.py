import os
from dotenv import load_dotenv
from flask_swagger_ui import get_swaggerui_blueprint

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    TESTING = False
    
class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
class DevelopmentConfig(Config):
    load_dotenv(os.path.join(BASE_DIR, '.env'))
    DEBUG = True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:903903@localhost:5432/memoria'
    
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': 'Aule API'
        }
    )
    
class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'test'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'test.db')
    
    WTF_CSRF_ENABLED = False