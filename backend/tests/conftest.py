import pytest
from app import create_app
from config import TestingConfig

from app.extensions import db
from app.models import Aule, User, Application, Chapter, Question, Student, Score


@pytest.fixture(scope='module') 
def test_client():
    flask_app = create_app(TestingConfig)
    
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client

@pytest.fixture(scope='module')
def create_base(test_client):
    db.create_all()
    
    test_school = School('Test School', 'Chillan Viejo', 'Ñuble')
    db.session.add(test_school)
    
    test_user = User('test_user', 'seba@test.cl', 'testtest')
    db.session.add(test_user)
    
    test_mobile_app = Application('TESAPP', 'Test App')
    db.session.add(test_mobile_app)
    
    db.session.commit()
    
    test_aule = Aule(test_mobile_app.id, 'Test Aule', test_user.id, test_school.id, 'TESAU1') 
    db.session.add(test_aule)
    
    test_aule_2 = Aule(test_mobile_app.id, 'Test Aule 2', test_user.id, test_school.id, 'TESAU2')
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
    
    db.session.delete(test_student)
    db.session.delete(test_student_2)
    db.session.delete(test_student_3)
    db.session.commit()
    
@pytest.fixture(scope='module')
def fill_app_mobile(test_client, create_base):
    test_chapter = Chapter('TESCHA', 'Test Chapter', 'TESAPP')
    db.session.add(test_chapter)
    
    test_chapter_2 = Chapter('TESCH2', 'Test Chapter 2', 'TESAPP')
    db.session.add(test_chapter_2)
    
    
    test_question = Question('TESQUE', 'Test Question', test_chapter.id)
    db.session.add(test_question)
    
    test_question_2 = Question('TESQU2', 'Test Question 2', test_chapter.id)
    db.session.add(test_question_2)
    
    test_question_3 = Question('TESQU3', 'Test Question 3', test_chapter_2.id)
    db.session.add(test_question_3)
    db.session.commit()
    
    yield [test_chapter, test_chapter_2, test_question, test_question_2, test_question_3]
    
@pytest.fixture(scope='function')
def create_scores(test_client, create_base, create_students, fill_app_mobile):
    test_student = create_students[0]
    test_student_2 = create_students[1]

    
    test_question = fill_app_mobile[2]
    test_question_2 = fill_app_mobile[3]
    test_question_3 = fill_app_mobile[4]
    
    score = Score(test_student.id, test_question.id, seconds=10000, is_correct=1)
    db.session.add(score)
    
    score_2 = Score(test_student.id, test_question_2.id, seconds=20000, is_correct=2)
    db.session.add(score_2)
    
    score_3 = Score(test_student_2.id, test_question.id, seconds=30000, is_correct=3)
    db.session.add(score_3)
    
    score_4 = Score(test_student_2.id, test_question_2.id, seconds=40000, is_correct=4)
    db.session.add(score_4)
    
    score_5 = Score(test_student_2.id, test_question_3.id, seconds=50000, is_correct=5)
    db.session.add(score_5)
    
    db.session.commit()
    
    yield [score, score_2, score_3, score_4, score_5]
    
    db.session.delete(score)
    db.session.delete(score_2)
    db.session.delete(score_3)
    db.session.delete(score_4)
    db.session.delete(score_5)
    db.session.commit()