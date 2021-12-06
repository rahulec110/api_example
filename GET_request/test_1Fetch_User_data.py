"""Required requests, json, jsonpath
  Need to install requests and jsonpath"""

import requests

# API url
url = "https://reqres.in/api/users?page=2"  #Base url then relative url

#Send get request
response = requests.get(url)
print(response)
"""print(response.status_code)
print(response.text)
print(response.cookies)"""

#Display response content
print(response.content)
print()
print(response.headers)