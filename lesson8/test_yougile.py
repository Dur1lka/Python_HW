import requests
import pytest

base_url = "https://ru.yougile.com/api-v2"
token="J-S8sJLjlz1OKnFKwXP5M8E4S2ZAbF4m85xK4M26owYmw0Q2XgviwdSlCzhwFIKP"

# Позитивный тест на создание проекта
def test_create_project():
    headers={
        'Authorization': f"Bearer {token}",
        'Content-Type': "application/json"
    }
    project={
        "title":"Python92"
             } 
    resp=requests.post(base_url + '/projects',
                       headers=headers,
                       json=project)
    response_data=resp.json()
    assert resp.status_code==201

# Негативный тест на создание проекта
def test_create_project_2():
    headers={
        'Authorization': f"Bearer {token}",
        'Content-Type': "application/java"
    }
    project={
        "title":123
             }
    resp=requests.post(base_url + '/projects',
                       headers=headers,
                       json=project)
    response_data=resp.json()
    assert resp.status_code==400
    
  

# Позитивная проверка изменения проекта
def test_update_project():
    headers={
        'Authorization': f"Bearer {token}",
        'Content-Type': "application/json"
    }
    project={
        "title":"Python123"
             } 
    resp=requests.post(base_url + '/projects',
                       headers=headers,
                       json=project)
    response_data=resp.json()
    project_id=response_data["id"]
    new_project_name={
        "title":"Skypro"
             } 
    resp2=requests.put(base_url + '/projects/' + project_id,
                       headers=headers,
                       json=project)
    response_data_2=resp2.json()
    print(response_data_2)
    assert resp.status_code==201
    assert response_data_2["id"]==project_id

# Негативная проверка изменения проекта
def test_update_project_2():
    headers={
        'Authorization': f"Bearer {token}",
        'Content-Type': "application/json"
    }
    project={
        "title":"Python123"
             } 
    resp=requests.post(base_url + '/projects',
                       headers=headers,
                       json=project)
    response_data=resp.json()
    project_id=response_data["id"]
    resp2=requests.put(base_url + '/projects/' + "123",
                       )
    response_data_2=resp2.json()
    assert resp2.status_code==401
    
# позитивная проверка получить ID
def test_get_project():
    headers={
        'Authorization': f"Bearer {token}",
        'Content-Type': "application/json"
    }
    project={
        "title":"Python92"
             } 
    resp=requests.post(base_url + '/projects',
                       headers=headers,
                       json=project)
    response_data=resp.json()
    id=response_data["id"]
    get_response=requests.get(base_url + '/projects' + id,
                              headers=headers
                              )
    assert resp.status_code==201

# негативная проверка получить ID
def test_get_project_2():
    headers={
        'Authorization': f"Bearer {token}",
        'Content-Type': "application/json"
    }
    project={
        "title":"Python92"
             } 
    resp=requests.post(base_url + '/projects',
                       headers=headers,
                       json=project)
    response_data=resp.json()
    id=response_data["id"]
    get_response=requests.get(base_url + '/projects' + id,
                              )
    assert get_response.status_code==401
