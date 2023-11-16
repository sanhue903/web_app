import pytest
from app.student.routes import create_student
from app.models.student import Student 

test_student = { 
    'first_name': 'Sebastian',
    'last_name': 'Sanhueza',
    'last_name_2': 'Bustamante',
    'age': 22,
    'aule_id': 1
}
test_student_2 = {
    'first_name': 'Sofia',
    'last_name': 'Riquelme',
    'last_name_2': 'Irribarra',
    'age': 23,
    'aule_id': 1
}


def test_create_student(test_client, create_aule):
    student = create_student(test_student)
    assert isinstance(student, Student)
    
#def test_error_create_student(test_client, create_aule):

def test_post_student(test_client, create_aule):
    response = test_client.post('/students', json=test_student)
    assert response.status_code == 201
    assert response.json['student']['first_name'] == test_student['first_name']
    
def test_error_post_student_aule_dont_exist(test_client, create_aule):
    student = {
        'first_name': 'Sebastian',
        'last_name': 'Sanhueza',
        'last_name_2': 'Bustamante',
        'age': 22,
        'aule_id': 2
    }
    response = test_client.post('/students', json=student)
    assert response.status_code == 404

#def test_error_post_student_missing_data(test_client, create_aule):

def test_get_all_students(test_client, create_aule):
    test_client.post('/students', json=test_student).status_code
    test_client.post('/students', json=test_student_2).status_code
    
    response = test_client.get('/students')
    assert response.status_code == 200
    assert response.json['students'][0]['first_name'] == test_student['first_name']
    assert response.json['students'][1]['first_name'] == test_student_2['first_name']
    
def test_get_all_students_by_aule(test_client, create_aule):
    test_client.post('/students', json=test_student).status_code
    test_client.post('/students', json=test_student_2).status_code
    
    response = test_client.get('/students?aule_id=1')
    assert response.status_code == 200
    assert response.json['students'][0]['first_name'] == test_student['first_name']
    assert response.json['students'][1]['first_name'] == test_student_2['first_name']

def test_error_get_all_students_by_aule(test_client, create_aule):
    response = test_client.get('/students?aule_id=2')
    assert response.status_code == 404    
    
def test_get_one_student(test_client, create_aule):
    test_client.post('/students', json=test_student).status_code
    
    reponse = test_client.get('/students/1')
    assert reponse.status_code == 200
    assert reponse.json['students']['first_name'] == test_student['first_name']
    
def test_error_get_one_student(test_client, create_aule):
    response = test_client.get('/students/1')
    assert response.status_code == 404