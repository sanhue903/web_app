import pytest

def test_get_student_from_app(test_client, create_students):
    response = test_client.get('/apps/TESAPP/students')
    
    assert response.status_code == 200
    assert len(response.json['students']) == 3

def test_eror_get_student_from_app(test_client, create_students):
    response = test_client.get('/apps/NOOAPP/students')
    
    assert response.status_code == 404
    
def test_get_student_from_aule(test_client, create_students):
    response = test_client.get('/apps/TESAPP/aules/TESAU1/students')
    
    assert response.status_code == 200
    assert len(response.json['students']) == 2
    
def test_error_get_student_from_aule(test_client, create_students):
    response = test_client.get('/apps/TESAPP/aules/TESAU3/students')
    assert response.status_code == 404
    
    response = test_client.get('/apps/NOOAPP/aules/TESAU1/students')
    assert response.status_code == 404
    
