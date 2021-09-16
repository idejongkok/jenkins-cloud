import requests
import json
import jsonpath
import pytest

def test_get_all_users():
    url = 'http://api.noobtest.id/dummy/v1/users'
    response = requests.get(url)
    Code = response.status_code
    assert Code == 200
    
def test_post_user():
    url = 'http://api.noobtest.id/dummy/v1/users'
    query = {'email' : 'Test@email.com','name':'jono'}
    response = requests.post(url,json=query)
    Code = response.status_code
    assert Code == 200
    json_response = json.loads(response.text)
    Name = jsonpath.jsonpath(json_response,'name')
    assert Name[0] == 'jono'