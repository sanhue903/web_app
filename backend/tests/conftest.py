import pytest
from app import create_app
from config import TestingConfig

from app.extensions import db
from app.models.aule import Aule
from app.models.user import User
from app.models.school import School

@pytest.fixture(scope='module') 
def test_client():
    flask_app = create_app(TestingConfig)
    
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client

@pytest.fixture(scope='function')
def create_aule(test_client):
    db.create_all()
    
    test_school = School('Test School', 'Chillan Viejo', 'Ñuble')
    db.session.add(test_school)
    
    test_user = User('test_user', 'test@gmail.cl', 'sebastian', 'sanhueza')
    db.session.add(test_user)
    
    db.session.commit()
    
    test_aule = Aule('Aula 1', test_school.id, test_user.id)
    db.session.add(test_aule)
    
    db.session.commit()
    
    yield 
    
    db.drop_all()