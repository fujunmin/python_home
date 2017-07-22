#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入第三方库
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# 导入自定义库
from com.EntList import enterpriseListPro
from com.constants import GET_OK

class TestEntListPro(unittest.TestCase):
    """仅测试关于enterpriseListPro方法相关代码"""
    def test_1(self):
        """有效企业名称：汉柏科技有限公司"""
        ret = enterpriseListPro("汉柏科技有限公司")
        # print len(ret["ENTERPRISES"]), ret["ENTERPRISES"]
        assert ret["CODE"] == GET_OK and len(ret["ENTERPRISES"]) != 0

    def test_2(self):
        """无效企业名称：%#%$#"""
        ret = enterpriseListPro("%#%$#^")
        # print len(ret["ENTERPRISES"]), ret["ENTERPRISES"]
        assert ret["CODE"] == GET_OK and len(ret["ENTERPRISES"]) == 0