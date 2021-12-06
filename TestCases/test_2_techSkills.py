import requests
import json

#@pytest.mark.skip
def test_1_get():
    url = "http://thetestingworldapi.com/api/technicalskills"
    responce = requests.get(url)
    print(responce.status_code)
    assert responce.status_code == 200, 'response not valid'
    print(responce.headers)
    print(responce.headers.get('Content-Length'))
#@pytest.mark.skip
def test_2_get():
    url = "http://thetestingworldapi.com/api/technicalskills/{id}"
    responce = requests.get(url)
    print(responce.status_code)
    print(responce.headers)
    print(responce.headers.get('Content-Length'))
    assert responce.headers.get('Content-Type') == 'application/json; charset=utf-8'
#@pytest.mark.skip
def test_3_post():
    url = "http://thetestingworldapi.com/api/technicalskills"
    file=open('/home/rahul/Desktop/API/post_technical_skills.json','r')
    request_json=json.loads(file.read()) #parse the data in json format
    print(request_json)

    response= requests.post(url,request_json)
    print(response.content)
    print(response.status_code)
    print(response.headers)
    '''
    Read input json from file > Parse into json format > Hit post method > Parse response to json format > Validate response.
    '''
def test_4_put():
    url= "http://thetestingworldapi.com/api/technicalskills/{id}"
    file=open('/home/rahul/Desktop/API/put_technical_skill.json','r')
    request_json=json.loads(file.read())
    print(request_json)

    response=requests.put(url,request_json)
    assert response.status_code==400, 'Invalid Response status code'
    print(response.headers)
    print(response.text)
    #print(response.content)

    response_json=json.loads(response.text)
    print(response_json)

def test_5_delete():
    url = "http://thetestingworldapi.com/api/technicalskills/{id}"
    response=requests.delete(url)
    assert response.status_code==400,'Invalid Response status code'
    print(response.content)
    print(response.text)
    print(response.headers)
    print(response.headers.get('Date'))