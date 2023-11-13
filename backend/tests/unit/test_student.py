import pytest
from app.student.routes import create_student
from app.models.student import Student 

def test_create_student(test_client, create_aule):
    json={
        'first_name': 'Sebastian',
        'last_name': 'Sanhueza',
        'last_name_2': 'Bustamante',
        'age': 22,
        'aule_id': 1
    }
    
    student = create_student(json)
    assert isinstance(student, Student)
    
def test_error_create_student(test_client, create_aule):
    json={
        'first_name': 'Sofia',
        'last_name': 'Riquelme',
        'last_name_2': 'Irribarra',
        'aule_id': 1
    }
    
    student = create_student(json)
    assert student is None
    
