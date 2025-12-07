import requests
import pytest
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("token")
base_url = "https://ru.yougile.com/api-v2"

def test_create_project():
    headers={
        'Authorization': f"Bearer{token}",
        'Content-Type': "aplication/json"
    }
data={"title":"Python92"}
resp=requests.post(base_url + '/projects')
response_data=resp.json()
assert resp.status_code==201
