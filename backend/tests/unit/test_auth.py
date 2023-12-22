import pytest

def test_sign_up(test_client, create_base):
    response = test_client.post('/auth/signup', json={
        'username': 'test_user2',
        'email': 'test@test.cl',
        'password': 'testtest',
        'confirm_password': 'testtest'
    })

    assert response.status_code == 201
    
def test_error_username_sign_up(test_client, create_base):
    response = test_client.post('/auth/signup', json={
        'username': 'test_user',
        'email': 'test_user@test.cl',
        'password': 'testtest',
        'confirm_password': 'testtest'
    })
    
    assert response.status_code == 409
    
def test_error_email_sign_up(test_client, create_base):
    response = test_client.post('/auth/signup', json={
        'username': 'test_user2',
        'email': 'seba@test.cl',
        'password': 'testtest',
        'confirm_password': 'testtest'
    })
    
    assert response.status_code == 409
    
def test_error_confirm_password_sign_up(test_client, create_base):
    response = test_client.post('/auth/signup', json={
        'username': 'test_user3',
        'email': 'test3@test.cl',
        'password': 'testtest',
        'confirm_password': 'testtest2'
    })
    
    assert response.status_code == 400

def test_login(test_client, create_base):
    response = test_client.get('/auth/login', json={
        'username': 'test_user',
        'password': 'testtest'
    })

    assert response.status_code == 200
    
def test_error_login(test_client, create_base):
    response = test_client.get('/auth/login', json={
        'username': 'test_user',
        'password': 'testtest2'
    })
    
    assert response.status_code == 401