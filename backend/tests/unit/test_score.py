import pytest

def test_get_all_scores_from_aule(test_client, create_base, create_students, fill_app_mobile, create_scores):
    response = test_client.get('/apps/TESAPP/aules/TESAU1/students/scores')
    
    assert response.status_code == 200
    assert len(response.json['results']) == 2
    assert len(response.json['results'][0]['chapter']['question']) == 2
    assert response.json['results'][0]['chapter']['question'][0]['score'][0]['attempts'] == 1
    assert response.json['results'][0]['chapter']['question'][0]['score'][0]['miliseconds'] == 10000
    assert response.json['results'][0]['chapter']['question'][0]['score'][1]['attempts'] == 3
    assert response.json['results'][1]['chapter']['question'][0]['score'][0]['miliseconds'] == 50000
    
def test_get_all_scores_from_aule_not_found(test_client, create_base, create_students, fill_app_mobile, create_scores):
    response = test_client.get('/apps/NOOAPP/aules/TESAU2/students/scores')
    
    assert response.status_code == 404
    
    response = test_client.get('/apps/TESAPP/aules/NOOAULE/students/scores')
    
    assert response.status_code == 404

    
