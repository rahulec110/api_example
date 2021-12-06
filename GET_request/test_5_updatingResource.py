import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

#Read input JSON file
file = open('/home/rahul/Desktop/API/CreateUser.json','r')
json_input = file.read()
request_json = json.loads(json_input) # parse the data in json format
print(request_json)

response= requests.put(url,request_json)
assert response.status_code==200, "Code not matching"
print(response.content)

#Parse response to json format
response_json=json.loads(response.text)
print(response_json)

updated_li = jsonpath.jsonpath(response_json,'updatedAt')
print(updated_li[0])