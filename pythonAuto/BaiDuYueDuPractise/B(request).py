import requests
import json
def login():
    username = 'gaoqicui'
    password = 'admin'
    test_url = 'http://192.168.201.72:8088/api/user/login'
    form_data = {'username': username, 'password': password}
    login_response = requests.post(test_url, data=form_data)

def inquire():
    cookie, user_id = login()  #根据顺序分别把第一个值赋给cookie，第二个值赋给user_id
    test_url = 'http://xxx.com/inquire'
    form_data = {'id': user_id}
    login_response = requests.post(test_url, data=form_data, cookies=cookie)
    r = login_response.text
    print(r)
if __name__ == "__main__":
    login()
    inquire()

