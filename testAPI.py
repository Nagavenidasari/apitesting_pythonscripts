import requests
import json
import pytest

# python -m pytest -v -s testAPI.py

url = 'https://reqres.in/api/'
user = 'users/2'

def test_get_endpoint():
    response = requests.get(url+user)
    assert response.status_code==200
    print(response)

def test_auth_request():
    jsonPayload = {
        "email":"eve.holt@reqres.in",
        "password":"cityslickaa"
    }
    response = requests.post(url+"login",json=jsonPayload)
    assert response.status_code==200
    # json.loads() method of json module parses the response 
    #string and concerts it intoa python dictionary that helps in accessing json easily with in the code.
    json_response=json.loads(response.text) 
    token=json_response["token"]
    print(token)

def test_createUser_request():
    jsonPayload = {
        "name":"Jason",
        "job":"teacher"
    }
    response = requests.post(url+"users",json=jsonPayload)
    assert response.status_code==201
    json_response=json.loads(response.text) 
    id1 = json_response["id"]
    if "id" in json_response:
        print(id1)
    else:
        print("not found")

def test_updateUser_request():
    jsonPayload = {
        "name":"Jason",
        "job":"businessman" #changed from teacher to businessman
    }
    response = requests.put(url+"users/2",json=jsonPayload)
    assert response.status_code==200
    json_response=json.loads(response.text)
    print(json_response)
    job = json_response["job"]
    print(job)
    assert response.json()["job"]=="businessman"
    assert job == "businessman"
    #assert json_response.get('job') == 'teacher' # should fail as job is updated

def test_deleteUser_request():
    response = requests.delete(url+"users/2")
    assert response.status_code==204