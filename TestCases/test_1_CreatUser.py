import requests
import json
import jsonpath

url = "https://reqres.in/api/users"

def test_create_user():
    # Read input JSON file
    file = open('/home/rahul/Desktop/API/CreateUser.json', 'r')
    json_input = file.read()  # files in string format
    request_json = json.loads(json_input)  # parse the data in json format
    print(request_json)
    print()

    # Make POST request with json input body
    response = requests.post(url, request_json)

    # validating response code
    assert response.status_code == 201
    print(response.content)
    print()

   # Fetch header from response
    print(response.headers)
    print('Content length : ',response.headers.get('Content-Length'))
    print()

    # Parse response to json format
    response_json = json.loads(response.text)
    print(response_json)

    # Pick id using json path
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])

def test_update_User():
    url = "https://reqres.in/api/users/2"

    # Read input JSON file
    file = open('/home/rahul/Desktop/API/CreateUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)  # parse the data in json format
    print(request_json)

    response = requests.put(url, request_json)
    assert response.status_code == 200, "Code not matching"

    # Parse response to json format
    response_json = json.loads(response.text)
    print(response_json)

    updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
    print(updated_li[0])