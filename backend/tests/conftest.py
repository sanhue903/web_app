import pytest
from app import create_app
from config import TestingConfig

from app.extensions import db
from app.models.aule import Aule
from app.models.user import User
from app.models.school import School
from app.models.mobile.mobile_app import MobileApp
from app.models.mobile.chapter import Chapter
from app.models.mobile.question import Question


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
    
@pytest.fixture(scope='module')
def create_app_mobile(test_client):
    test_mobile_app = MobileApp('TESAPP', 'Test App')
    test_chapter = Chapter('TESCHA', 'Test Chapter', test_mobile_app.id)
    test_question = Question('TESQUE', 'Test Question', test_chapter.id)