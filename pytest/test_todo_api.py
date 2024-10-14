#https://todo.pixegami.io

#get, put,patch, post,delete
#status_code: 2xx, 3xx, 4xx, 5xx
#pip3 install requests
#pip3 install pytest
#body, params, header
import requests
# from requests import get

#case 1:
    # success
ENDPOINT = "https://todo.pixegami.io"


# print(status_code)

def test_call_api_create_task():
    payload = {
      "content": "string",
      "user_id": "user1",
      "task_id": "string",
      "is_done": False
    }
    response = requests.put(ENDPOINT + "/create-task", json=payload)

    data = response.json()
    print(data)

    status_code = response.status_code
    assert status_code == 200
    
    user_id = data["task"]["user_id"]
    assert user_id == "user1"

def test_call_api_get_task():
   
    task_id = 'task_75606a9706274644932b12edce980059'
    response = requests.get(ENDPOINT + f"/get-task/{task_id}")

    data = response.json()
    print(data)

    status_code = response.status_code
    assert status_code == 200
    
    task_content = data["content"]
    
    assert task_content == "string1"
    
    