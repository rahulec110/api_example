import requests
import json
import jsonpath

url = "https://reqres.in/api/users"

'''
POST : is used for Creating a new resources on the server
PUT  : is used for Updating data on the server
in both the case need to send request body
'''

#Read input JSON file
file = open('/home/rahul/Desktop/API/CreateUser.json','r')
json_input = file.read() # files in string format
request_json = json.loads(json_input)  # parse the data in json format from string format
print(request_json)
print()

#Make POST request with json input body
response = requests.post(url,request_json)

#validating response code
assert response.status_code== 201
print(response.content)
print()

#Fetch header from response
print(response.headers)
print(response.headers.get('Content-Length'))
print()

#Parse response to json format
response_json = json.loads(response.text)
print(response_json)

#Pick id using json path
id = jsonpath.jsonpath(response_json,'id')
print(id[0])