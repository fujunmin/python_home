#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入第三方库
from urlparse import urljoin
# 导入自定义库
from lib.rest import RestUtil
# 导入配置文件
from global_config import BASEPATH

# 企业名录专业版
def enterpriseListPro(key, areaCode=None, industryPhy=None, entStatus=None, regcapGte=None, regcapLte=None, enableAggregate=False, page=None, size=20):
    """
    :document: enterpriseListPro(企业名录专业版), 输入企业名称返回企业列表
    :param key: string,查询企业的名称
    :param areaCode: string,区域代码
    :param industryPhy: string,行业代码
    :param entStatus: string,企业经营状态，1：在营，2：吊销，3：注销，4：迁出，8：停业，9：其他，9_01：撤销，9_02：待迁入，9_03：经营期限届满；9_04：清算中；9_05：停业
    :param regcapGte: string,最小注册资本（万元）
    :param regcapLte: string,最大注册资本（万元）
    :param enableAggregate: string,是否按照区域代码和行业代码统计数量,统计:true，不统计:false(默认选项)
    :param page: integer,当前页数
    :param size: integer,每页返回的数据数量
    :return:
    """

    # 拼接url
    uri = urljoin(BASEPATH, "enterprises")

    # 组装body
    params = {}
    params["key"] = key
    params["areaCode"] = areaCode
    params["industryPhy"] = industryPhy
    params["entStatus"] = entStatus
    params["regcapGte"] = regcapGte
    params["regcapLte"] = regcapLte
    params["enableAggregate"] = enableAggregate
    params["page"] = page
    params["size"] = size

    # 发送http请求
    req = RestUtil()
    ret = req.get(uri, params)
    if ret:
        return ret
    else:
        return False

# 企业名录通用版
def enterpriseListBasic(key, page=None, size=20):
    """
    :document: enterpriseListBasic(企业名录通用版), 输入企业名称返回企业列表
    :param key: string,查询企业的名称
    :param page: integer,当前页数
    :param size: integer,每页返回的数据数量
    :return:
    """

    # 拼接url
    uri = urljoin(BASEPATH, "enterprisesList/basic")

    # 组装body
    params = {}
    params["key"] = key
    params["page"] = page
    params["size"] = size

    # 发送http请求
    req = RestUtil()
    ret = req.get(uri, params)
    if ret:
        return ret
    else:
        return False