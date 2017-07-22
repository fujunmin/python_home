#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, requests, time, hashlib

from global_config import UID, SECURITY_KEY


class RestRequestError(Exception):
    pass

class RestRequest(object):
    """
    用于发送和处理HTTP的REST请求
    """

    def __init__(self, uid=None, security_key=None):
        self.uid = uid
        self.security_key = security_key
        self.timestamp = ""
        self.nonce = ""
        self.signature = ""

        if not uid:
            self.uid = UID
            self.security_key = SECURITY_KEY

        self.nonce = str(random.randint(-999999999, 999999999))
        self.timestamp = str(int(time.time()* 1000))
        self.signature = hashlib.sha1(self.nonce+ ";"+ self.security_key+ ";"+ self.timestamp+ ";"+ self.uid+ ";").hexdigest()

        self.default_headers = {
            "Content-Type": "application/json",
            "X-Uid": self.uid,
            "X-Nonce": self.nonce,
            "X-Timestamp": self.timestamp,
            "X-Signature": self.signature
            }

    def _send_request(self, uri, method, params=None, headers=None):
        if not uri:
            raise RestRequestError("Error: URI is emtpy!")

        try:
            session = requests.Session()
            if not headers:
                headers = self.default_headers
            if method == "GET":
                req = requests.get(uri, params, headers=headers)
            elif method == "PUT":
                req = requests.put(uri, params, headers=headers)
            elif method == "POST":
                req = requests.post(uri, params, headers=headers)
            elif method == "DELETE":
                req = requests.delete(uri, params, headers=headers)
            else:
                raise RestRequestError("Error: Method:%s is not http method!") % method
            req.raise_for_status()
            result = req.json()
        except Exception, e:
            raise RestRequestError("HTTPConnection Error: %s" % e)
        finally:
            if session:
                session.close()
        return result

    def get(self, uri, params=None, headers=None):
        return self._send_request(uri, "GET", params, headers)

    def post(self, uri, params=None, headers=None):
        return self._send_request(uri, "POST", params, headers)

    def put(self, uri, params=None, headers=None):
        return self._send_request(uri, "PUT", params, headers)

    def delete(self, uri, params=None, headers=None):
        return self._send_request(uri, "DELETE", params, headers)

class RestUtil(object):
    """
    简化对RestRequest来的操作
    """

    @classmethod
    def get(cls, uri, params, headers=None):
        rest = RestRequest()
        result = rest.get(uri, params, headers)
        return result

    @classmethod
    def post(cls, uri, params, headers=None):
        rest = RestRequest()
        return rest.post(uri, params, headers)

    @classmethod
    def put(cls, uri, params, headers=None):
        rest = RestRequest()
        return rest.put(uri, params, headers)

    @classmethod
    def delete(cls, uri, params, headers=None):
        rest = RestRequest()
        return rest.delete(uri, params, headers)


# 测试RestRequest get
# rest = RestRequest()
# default_headers = {
#     "Content-Type": "application/json",
#     "X-Uid":UID,
#     "X-Nonce":NONCE,
#     "X-Timestamp":TIMESTAMP,
#     "X-Signature":SIGNATURE
# }
# req = rest.get("https://testapi.bidata.com.cn/platform/v3/enterprises",{"key":"汉柏科技"},default_headers)
# print req
# for i in req:
#     print i,req[i]

# 测试RestUtil get
# rest = RestUtil
# default_headers = {
#     "Content-Type": "application/json",
#     "X-Uid":UID,
#     "X-Nonce":NONCE,
#     "X-Timestamp":TIMESTAMP,
#     "X-Signature":SIGNATURE
# }
# req = rest.get("https://testapi.bidata.com.cn/platform/v3/enterprises",{"key":"汉柏科技"},default_headers)
# print req
# for i in req:
#     print i,req[i]

#测试requests get
# url="https://testapi.bidata.com.cn/platform/v3/enterprises?key=汉柏科技 彭海帆"
# default_headers = {
#     "Content-Type": "application/json",
#     "X-Uid":UID,
#     "X-Nonce":NONCE,
#     "X-Timestamp":TIMESTAMP,
#     "X-Signature":SIGNATURE
# }

# s = requests.Session()
# s.verify="C:\Users\aaa\PycharmProjects\apitest\api.bidata.com.cn.jks"
# s.verify="api.bidata.com.cn.jks"
# req = requests.get(url,headers=default_headers)
# requests.get
# print req.content
