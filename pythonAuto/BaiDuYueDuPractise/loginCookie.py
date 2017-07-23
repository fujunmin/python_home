#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
# import certifi
# import urllib3
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
url="https://passport.cnblogs.com/user/signin"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
}
s=requests.session()
# coo=requests.cookies.RequestsCookieJar()
# coo.set('cookie-name','cookie-value',path='/',domain='.cnblogs.com')
# s.cookies.update(coo)

r=s.get(url,headers=headers,verify=False)
print(s.cookies)
c=requests.cookies.RequestsCookieJar()
c.set('.CNBlogsCookie','0F92EDF64313FD346F3DE45730CA203FD4D6C780B8C33D7DA120DA387433009BBA9F10D20CF92A269B81392C6244DD4D9932BE71A46C8ED8DEFB360DCC862D854BD1C5185B8D1EC5BCBB1D4899E8AA324ADF0339')
c.set('.Cnblogs.AspNetCore.Cookies','CfDJ8PhlBN8IFxtHhqIV3s0LCDml7EBotIFtJF09nJ6nMtS7tUwZ_1wBco3HN-gd7U451E2-o_-bMl_mnGy8jkG5C1430kmx2HO5tW-XirtmzN1NclZu5mGqtWlgOVVrnlthZsAFGyhtiq3_ywm5vVRa8T45Lht5QecGmfsqFIdkEWEV3L2a9nLMRUEzCu455iJG80VDJ150A3wUrxR0AqmG4rLzPCDoh38VZkCL7PR98FF1QqITomVMVfUoFV6jGxnE-2-dCFCFWuPpNWJy_M2VQPwlDx7x3BWkJcWJ1_OX5PjDPEXuOMtohPka_Ii7l0-n7A')
print(s.cookies)

url2="https://i.cnblogs.com/EditPosts.aspx?opt=1"
body={
    "__VIEWSTATE":"",
    "__VIEWSTATEGENERATOR":"FE27D343",
    "Editor$Edit$txbTitle":"titletesting2",
    "Editor$Edit$EditorBody":"<p>this is content2</p>",
    "Editor$Edit$Advanced$ckbPublished":"on",
    "Editor$Edit$Advanced$chkDisplayHomePage":"on",
    "Editor$Edit$Advanced$chkComments":"on",
    "Editor$Edit$Advanced$chkMainSyndication":"on",
    "Editor$Edit$lkbDraft":"存为草稿"
}

r2=s.post(url2,data=body,verify=False)
print(str(r2.content))


