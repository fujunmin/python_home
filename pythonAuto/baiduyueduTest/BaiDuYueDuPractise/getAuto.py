import  requests


import json
url="https://status.github.com/api/status.json"
response = requests.get(url)
r = response.text
#h = response.header
print(r)
#print(h)



