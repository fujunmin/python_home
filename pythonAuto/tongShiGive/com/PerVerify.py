#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入第三方库
from urlparse import urljoin
# 导入自定义库
from lib.rest import RestUtil
# 导入配置文件
from global_config import BASEPATH

# 人企关联核验
def relation(name, entName, identity):
    """
    :document: entPerson(人企关联核验),验证人员是否和查询企业的有关联(董事、法人、管理)
    :param name: string,姓名
    :param entName: string,企业标识（输入：企业全称/注册号/组织机构代码/统一社会信用代码）
    :param identity: string,身份证号码验证是否是15或18位字符
    :return:
    """

    # 拼接url
    uri = urljoin(BASEPATH, "verify/relation")

    # 组装body
    params = {}
    params["name"] = name
    params["entName"] = entName
    params["identity"] = identity

    # 发送http请求
    req = RestUtil()
    ret = req.get(uri, params)
    if ret:
        return ret
    else:
        return False

# 电信三要素核验
def telecom(name, mobile, identity):
    """
    :document: telecom(电信三要素核验),验证姓名、手机号、身份证号码是否一致
    :param name: string,姓名
    :param mobile: string,手机号验证是否是11位数字
    :param identity: string,身份证号码验证是否是15或18位字符
    :return:
    """

    # 拼接url
    uri = urljoin(BASEPATH, "verify/telecom")

    # 组装body
    params = {}
    params["name"] = name
    params["mobile"] = mobile
    params["identity"] = identity

    # 发送http请求
    req = RestUtil()
    ret = req.get(uri, params)
    if ret:
        return ret
    else:
        return False

# 人员任职核验
def executive(name, entName, identity, personType=None):
    """
    :document: executive(人员任职核验),验证人员是否是查询企业的董事、法人、管理
    :param name: string,姓名
    :param entName: string,企业标识（输入：企业全称/注册号/组织机构代码/统一社会信用代码）
    :param identity: string,身份证号码验证是否是15或18位字符
    :param personType: string,人员类型(legal:法人,shareholder:股东,priperson:高管);
    :return:
    """

    # 拼接url
    uri = urljoin(BASEPATH, "verify/executive")

    # 组装body
    params = {}
    params["name"] = name
    params["entName"] = entName
    params["identity"] = identity
    params["personType"] = personType

    # 发送http请求
    req = RestUtil()
    ret = req.get(uri, params)
    if ret:
        return ret
    else:
        return False

# 人员任职核验v2
def executive2(name, entName, identity, personType=None):
    """
    :document: executive2(人员任职核验v2),验证人员是否是查询企业的董事、法人、管理
    :param name: string,姓名
    :param entName: string,企业标识（输入：企业全称/注册号/组织机构代码/统一社会信用代码）
    :param identity: string,身份证号码验证是否是15或18位字符
    :param personType: string,人员类型(legal:法人,shareholder:股东,priperson:高管);
    :return:
    """

    # 拼接url
    uri = urljoin(BASEPATH, "verify/executive/v2")

    # 组装body
    params = {}
    params["name"] = name
    params["entName"] = entName
    params["identity"] = identity
    params["personType"] = personType

    # 发送http请求
    req = RestUtil()
    ret = req.get(uri, params)
    if ret:
        return ret
    else:
        return False

# 企业名称一致性核验
def thrcheck(entId):
    """
    :document: thrcheck(企业名称一致性核验),企业名称在工商局、质监局、税务局登记一致性数据核验;entId企业标识（注册号/统一社会信用代码）
    :param entId: string,企业标识（注册号/统一社会信用代码）
    :return:
    """

    # 拼接url
    uri = urljoin(BASEPATH, "verify/thrcheck")

    # 组装body
    params = {}
    params["entId"] = entId

    # 发送http请求
    req = RestUtil()
    ret = req.get(uri, params)
    if ret:
        return ret
    else:
        return False