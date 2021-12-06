import jsonpath
import requests
import json

def test_add_student_data():
    url='http://thetestingworldapi.com/api/studentsDetails'
    file=open('/home/rahul/Desktop/API/student_details.json','r')
    request_json=json.loads(file.read())
    print(request_json)
    response= requests.post(url,request_json)
    print(response.content)
    print(response.text)

def test_update_student_data():
    url='http://thetestingworldapi.com/api/studentsDetails/453811'
    file= open('/home/rahul/Desktop/API/Updated_student_details.json','r')
    request_json= json.loads(file.read())
    print(request_json)
    response=requests.put(url,request_json)
    print(response.text)

def test_delete_student():
    url='http://thetestingworldapi.com/api/studentsDetails/453811'
    response=requests.delete(url)
    print(response.text)

def test_get_student_data():
    url='http://thetestingworldapi.com/api/studentsDetails/453811'
    response=requests.get(url)
    print(response.json())
    id=jsonpath.jsonpath(response.json(),'data.id')
    print(id)