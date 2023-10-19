import requests

endpoint_base = "http://localhost:8000/api/"


def create_student():
    endpoint = endpoint_base + "mobile/student/"
    data = {
        "first_name": "Camilo",
        "last_name": "Jarpa",
        "second_last_name": "Gutierrez",
        "age": 22,
    }
    get_response = requests.post(endpoint, json=data)

    print(get_response.text)
    print(get_response.status_code)
    
def create_score():
    endpoint = endpoint_base + "mobile/score/"
    data = {
        "attempts": 1,
        "duration": "00:00:01",
        "student": 1,
        "question": 1
    }
    
    get_response = requests.post(endpoint, json=data)

    print(get_response.text)
    print(get_response.status_code)
    
create_score()