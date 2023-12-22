import os
from flask_swagger_ui import get_swaggerui_blueprint

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORDS_QUERY = True
    
    JWT_SECRET_KEY = "super-secret"
    
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
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'test.db')
    
    WTF_CSRF_ENABLED = False