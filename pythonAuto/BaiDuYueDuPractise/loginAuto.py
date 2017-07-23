import requests
def login():
    username = ''
    password = ''
    test_url = 'http://xxx.com/login/'
    form_data = {'username': username, 'password': password}
    login_response = requests.post(test_url, data=form_data)
    c = login_response.cookies
    return c
def inquire():
    cookie = login()
    test_url = 'http://xxx.com/inquire'
    form_data = {'id': 54536}
    login_response = requests.post(test_url, data=form_data, cookies=cookie)
    r = login_response.text
    print(r)
if __name__ == "__main__":
    login()
    inquire()

