import pytest
from app import create_app
from config import TestingConfig

from app.extensions import db
from app.models import Aule, User, School, MobileApp, Chapter, Question, Student


@pytest.fixture(scope='module') 
def test_client():
    flask_app = create_app(TestingConfig)
    
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client

@pytest.fixture(scope='function')
def create_base(test_client):
    db.create_all()
    
    test_school = School('Test School', 'Chillan Viejo', 'Ñuble')
    db.session.add(test_school)
    
    test_user = User('test_user', 'seba@test.cl', 'sebastian', 'sanhueza', '903903')
    db.session.add(test_user)
    
    test_mobile_app = MobileApp('TESAPP', 'Test App')
    db.session.add(test_mobile_app)
    
    db.session.commit()
    
    test_aule = Aule('TESAU1',test_mobile_app.id, 'Test Aule', test_user.id, test_school.id) 
    db.session.add(test_aule)
    
    test_aule_2 = Aule('TESAU2',test_mobile_app.id, 'Test Aule 2', test_user.id, test_school.id)
    db.session.add(test_aule_2)
    
    db.session.commit()
    
    yield 
    
    db.drop_all()
    
@pytest.fixture(scope='function')    
def create_students(test_client, create_base):
    test_student = Student('Sebastian', 'Sanhueza', 'Bustamante', 22, 'TESAU1', 'TESAPP')
    db.session.add(test_student)
    
    test_student_2 = Student('Sofia', 'Riquelme', 'Irribarra', 23, 'TESAU1', 'TESAPP')
    db.session.add(test_student_2)
    
    test_student_3 = Student('Camilo', 'Jarpa', 'Gutierrez', 22, 'TESAU2', 'TESAPP')
    db.session.add(test_student_3)
    
    db.session.commit()
    
    yield [test_student, test_student_2, test_student_3]
    
@pytest.fixture(scope='function')
def fill_app_mobile(test_client, create_base):
    mobile_app = db.get_or_404(Aule, 'TESAU1', description=f'Aule with id TESAU1 not found')
    
    test_chapter = Chapter('TESCHA', 'Test Chapter', mobile_app.id)
    test_question = Question('TESQUE', 'Test Question', test_chapter.id)
    
    yield [mobile_app, test_chapter, test_question]