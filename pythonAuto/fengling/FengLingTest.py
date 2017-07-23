import requests
import json
def login():
    username = 'gaoqicui'
    password = 'admin'
    test_url = 'http://192.168.201.72:8088/api/user/login'
    form_data = {'username': username, 'password': password}
    json_data = json.dumps(form_data) #转换成json的入参
    headers={'content-type','application/json' }
    login_response = requests.post(test_url, data=form_data, headers=headers)
    c = login_response.token
    return c
def inquire():
    token= login()  #根据顺序分别把第一个值赋给cookie，第二个值赋给user_id
    test_url = 'http://192.168.201.72:8088/api/changes'
    login_response = requests.post(test_url, header=token)
    r = login_response.text
    print(r)
if __name__ == "__main__":
    login()
    inquire()

