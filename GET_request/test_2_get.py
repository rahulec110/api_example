import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"  #Base url then relative url

#Send get request
response = requests.get(url)
print(response)
print(response.status_code)

#Parse response to json format
json_response = json.loads(response.text)
print(json_response)
print()

#Fetch value using json path
#jsonpath always returns list object
pages_1 = jsonpath.jsonpath(json_response,'total_pages')
assert pages_1[0] == 2

pages_2 = jsonpath.jsonpath(json_response,'total')
assert pages_2[0] == 12