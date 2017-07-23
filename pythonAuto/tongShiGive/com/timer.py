# -*- coding: utf-8 -*-

"""
定时器，用于定时执行一些方法
"""

import time
from lib.rest import RestUtil


def period_call(query_url, compare_func, timeout, interval=1):
    """
    周期性执行query_func，用compare_func判断query结果是否符合预期。
    如果一直没符合预期，达到timeout，抛出异常
    """
    count = 0
    while count <= timeout:
        status, result = RestUtil.get(query_url)
        if compare_func(status, result):
            break
        time.sleep(interval)
        count += interval
    else:
        raise Exception("Error: query %s timeout" % query_url)
