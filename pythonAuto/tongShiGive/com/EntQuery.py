#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入第三方库
from urlparse import urljoin
# 导入自定义库
from lib.rest import RestUtil
# 导入配置文件
from global_config import BASEPATH

# 照面信息查询
def entBasicInfo(id=None, creditcode=None, regno=None, enttype=1):
    """
    :document: EntInfo(照面信息查询),输入企业的id,统一信用代码或注册号返回企业详情
    :param id: string,中数企业ID
    :param creditcode: string,统一信用代码
    :param regno: string,企业注册号
    :param enttype: string,企业类型:1-企业 2-个人
    :return:
    """

    # 拼接url
    uri = urljoin(BASEPATH, "entBasicInfo")

    # 组装body
    params = {}
    params["id"] = id
    params["creditcode"] = creditcode
    params["regno"] = regno
    params["enttype"] = enttype

    # 发送http请求
    req = RestUtil()
    ret = req.get(uri, params)
    if ret:
        return ret
    else:
        return False

# 企业经营状态查询
def entOperationStateInfo(id=None, creditcode=None, regno=None, enttype=1):
    """
    :document: OperationState(查询企业经营状态),根据企业id，统一信用代码或注册号查询企业经营状态
    :param id: string,中数企业ID
    :param creditcode: string,统一信用代码
    :param regno: string,企业注册号
    :param enttype: string,企业类型:1-企业 2-个人
    :return:
    """

    # 拼接url
    uri = urljoin(BASEPATH, "entOperationStateInfo")

    # 组装body
    params = {}
    params["id"] = id
    params["creditcode"] = creditcode
    params["regno"] = regno
    params["enttype"] = enttype

    # 发送http请求
    req = RestUtil()
    ret = req.get(uri, params)
    if ret:
        return ret
    else:
        return False

# 企业年报查询
def entYearReportInfo(id=None, creditcode=None, regno=None, enttype=1):
    """
    :document: YearReport(企业年报查询),输入企业的id,统一信用代码，注册号返回企业年报信息
    :param id: string,中数企业ID
    :param creditcode: string,统一信用代码
    :param regno: string,企业注册号
    :param enttype: string,企业类型:1-企业 2-个人
    :return:
    """

    # 拼接url
    uri = urljoin(BASEPATH, "entYearReportInfo")

    # 组装body
    params = {}
    params["id"] = id
    params["creditcode"] = creditcode
    params["regno"] = regno
    params["enttype"] = enttype

    # 发送http请求
    req = RestUtil()
    ret = req.get(uri, params)
    if ret:
        return ret
    else:
        return False

# 风险信息查询
def entRiskInfo(id=None, creditcode=None, regno=None, enttype=1):
    """
    :document: entRiskInfo(风险信息查询),输入企业的id,统一信用代码，注册号返回企业风险信息(包含被执行人信息，失信被执行人信息，行政处罚信息，经营异常名录)
    :param id: string,中数企业ID
    :param creditcode: string,统一信用代码
    :param regno: string,企业注册号
    :param enttype: string,企业类型:1-企业 2-个人
    :return:
    """

    # 拼接url
    uri = urljoin(BASEPATH, "entRiskInfo")

    # 组装body
    params = {}
    params["id"] = id
    params["creditcode"] = creditcode
    params["regno"] = regno
    params["enttype"] = enttype

    # 发送http请求
    req = RestUtil()
    ret = req.get(uri, params)
    if ret:
        return ret
    else:
        return False

# 风险信息查询
def entTrademarkInfo(id=None, creditcode=None, regno=None, enttype=1):
    """
    :document: entRiskInfo(风险信息查询),输入企业的id,统一信用代码，注册号返回企业商标信息(其中MARKIMAGE是图片二进制编码的base64编码)
    :param id: string,中数企业ID
    :param creditcode: string,统一信用代码
    :param regno: string,企业注册号
    :param enttype: string,企业类型:1-企业 2-个人
    :return:
    """

    # 拼接url
    uri = urljoin(BASEPATH, "entTrademarkInfo")

    # 组装body
    params = {}
    params["id"] = id
    params["creditcode"] = creditcode
    params["regno"] = regno
    params["enttype"] = enttype

    # 发送http请求
    req = RestUtil()
    ret = req.get(uri, params)
    if ret:
        return ret
    else:
        return False

# 企业详情查询企业版
def entInfo(id=None, creditcode=None, regno=None, mask="1101000001000001000000000110001000", enttype=1):
    """
    :document: entinfo(企业详情查询企业版),输入企业的id,统一信用代码，注册号返回企业详情
    :param id: string,中数企业ID
    :param creditcode: string,统一信用代码
    :param regno: string,企业注册号
    :param mask: string,查询掩码
    :param enttype: string,企业类型:1-企业 2-个人
    :return:
    """

    # 拼接url
    uri = urljoin(BASEPATH, "entinfo")

    # 组装body
    params = {}
    params["id"] = id
    params["creditcode"] = creditcode
    params["regno"] = regno
    params["mask"] = mask
    params["enttype"] = enttype

    # 发送http请求
    req = RestUtil()
    ret = req.get(uri, params)
    if ret:
        return ret
    else:
        return False

# 企业统计信息查询
def entStatisticalInfo(id=None, creditcode=None, regno=None, mask="1101000001000001000000000110001000", enttype=1):
    """
    :document: entStatisticalInfo(企业统计信息查询),输入企业的id,统一信用代码，注册号统计企业信息
    :param id: string,中数企业ID
    :param creditcode: string,统一信用代码
    :param regno: string,企业注册号
    :param mask: string,查询掩码
    :param enttype: string,企业类型:1-企业 2-个人
    :return:
    """

    # 拼接url
    uri = urljoin(BASEPATH, "enterprises/statisticalInfo")

    # 组装body
    params = {}
    params["id"] = id
    params["creditcode"] = creditcode
    params["regno"] = regno
    params["mask"] = mask
    params["enttype"] = enttype

    # 发送http请求
    req = RestUtil()
    ret = req.get(uri, params)
    if ret:
        return ret
    else:
        return False