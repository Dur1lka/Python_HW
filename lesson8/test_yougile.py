import requests
import pytest
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("token")
base_url = "https://ru.yougile.com/api-v2"

# Позитивный тест на создание проекта
def test_create_project(self,title,users,user_name,password,companyID):
    key=self.get_token(user_name=user_name,password=password,companyID=companyID)
    headers={
        'Authorization': f"Bearer{token}",
        'Content-Type': "aplication/json"
    }
    project={
        "title":"Python92",
        "users": users
             }
    responce=project.create_project("Python92") 
    resp=requests.post(base_url + '/projects',
                       headers=headers,
                       json=project)
    response_data=resp.json()
    project_id=response_data["id"]
    assert resp.status_code==201
    assert project_id, "Project id is empty"
    return project_id

# Негативный тест на создание проекта
def test_create_project(self,title,users,user_name,password,companyID):
    key=self.get_token(user_name=user_name,password=password,companyID=companyID)
    headers={
        'Authorization': f"Bearer{token}",
        'Content-Type': "aplication/java"
    }
    project={
        "title":"Python92",
        "users": users
             }
    responce=project.create_project("Python92") 
    resp=requests.post(base_url + '/projects',
                       headers=headers,
                       json=project)
    response_data=resp.json()
    project_id=response_data["id"]
    assert resp.status_code==201
    assert project_id, "Project id is empty"
    return project_id
    
  

# Позитивная проверка изменения проекта
def test_update_project(setup_project):
    project_id = setup_project
    new_title = "Python87"
    response = setup_project.update_project(project_id, new_title)
    assert response.status_code == 200
    updated_project = updated_project.get_project(project_id)
    assert updated_project.json()["title"] == new_title

# Негативная проверка изменения проекта
def test_update_project(setup_project):
    project_id = setup_project
    response = setup_project.update_project(project_id, "")
    assert response.status_code == 400
