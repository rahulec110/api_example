import json
import requests
import jsonpath

def test_Add_new_data():
    app_url='http://thetestingworldapi.com/api/studentsDetails'
    file=open('/home/rahul/Desktop/API/student_details.json','r')
    request_json=json.loads(file.read())
    #print(request_json)
    response=requests.post(app_url,request_json)
    #print(response.text)
    id=jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    tech_api_url='http://thetestingworldapi.com/api/technicalskills'
    f= open('/home/rahul/Desktop/API/post_technical_skills.json','r')
    request_json=json.loads(f.read())
    request_json['id']=int(id[0])
    request_json['st_id'] = id[0]
    response= requests.post(tech_api_url,request_json)
    print(response.text)

    address_api_url='http://thetestingworldapi.com/api/addresses'
    f= open('/home/rahul/Desktop/API/post_address.json','r')
    request_json=json.loads(f.read())
    request_json['stId'] = id[0]
    response= requests.post(address_api_url,request_json)
    #print(response.text)

    final_details='http://thetestingworldapi.com/api/FinalStudentDetails/'+str(id[0])
    response=requests.get(final_details)
    print(response.text)