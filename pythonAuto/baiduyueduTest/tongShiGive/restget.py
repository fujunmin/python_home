# !/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.rest import RestUtil

contenttype="application/json"
timestamp="1477880605762"
nonce="-279565889"
uid="YJ1M71RC"
signature="26b6abcf8a732e2ca79a77f8a5a6d137e080b229"

url="https://testapi.bidata.com.cn/platform/v3/enterprises?key=汉柏科技"
default_headers = {
    "Content-Type": contenttype,
    "X-Uid":uid,
    "X-Nonce":nonce,
    "X-Timestamp":timestamp,
    "X-Signature":signature
}

uri = "https://testapi.bidata.com.cn/platform/v3/enterprises"
params = {"key":"汉柏科技"}

ret = RestUtil()
result = ret.get(uri,params)
print result