# !/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import requests
import time
import hashlib

from global_config import UID, SECURITY_KEY

uri = 'https://testapi.bidata.com.cn/platform/v3/enterprises'
data = {'key': '北京中数智汇科技股份有限公司'}

Timestamp = str(int(time.time() * 1000))
Nonce = str(random.randint(-999999999, 999999999))
Signature = hashlib.sha1(Nonce + ";" + SECURITY_KEY + ";" + Timestamp + ";" + UID + ";").hexdigest()

header = {
    'Content-Type': 'application/json;charset=utf-8',
    'X-Uid': UID,
    'X-Timestamp': Timestamp,
    'X-Signature': Signature,
    'X-Nonce': Nonce
}
print UID
print Nonce
print Timestamp
print Signature

req = requests.get(uri, data, headers=header)
req.raise_for_status()
result = req.json()
if result:
    print result



