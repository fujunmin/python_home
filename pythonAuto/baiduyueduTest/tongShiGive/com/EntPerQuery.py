#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入第三方库
from urlparse import urljoin
# 导入自定义库
from lib.rest import RestUtil
# 导入配置文件
from global_config import BASEPATH

# 企业人员探查
def entPerson(entName, personName):
    """
    :document: entPerson(企业人员探查),根据企业名称、人员姓名查询人员信息
    :param entName: string,中数企业ID
    :param personName: string,统一信用代码
    :return:
    """

    # 拼接url
    uri = urljoin(BASEPATH, "entperson")

    # 组装body
    params = {}
    params["entName"] = entName
    params["personName"] = personName

    # 发送http请求
    req = RestUtil()
    ret = req.get(uri, params)
    if ret:
        return ret
    else:
        return False
