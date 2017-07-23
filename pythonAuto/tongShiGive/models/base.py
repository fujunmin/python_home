# -*- coding: utf-8 -*-

"""
主要包括一些用于测试模型的基础类.
"""

import json


class BaseTestModel(object):
    """为所有的测试模型提供一些基础通用方法.
    注意所有的测试模型，都要继承这个类
    """

    def __init__(self, **kwargs):
        if kwargs:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_primitive(self):
        """返回一个字典，内容为这个对象的属性和属性值
        """
        d = {}
        d.update(self.__dict__)
        return d

    @classmethod
    def from_primitive(cls, data):
        """返回一个新的这个类的对象，
        对象中属性的值来自于给定的字典data
        """
        obj = cls(**data)
        return obj

    def to_json(self):
        """返回一个json格式的字符串,
        字符串内容为这个对象所具有的属性和属性值
        """
        return json.dumps(self, default=lambda o: o.__dict__)

    @classmethod
    def from_json(cls, data):
        """根据给定的json格式的字符串data，
        赋值给这个对象的所有属性
        """
        d = json.loads(data)
        return cls.from_primitive(d)

    @classmethod
    def from_result(cls, result):
        """
        根据HTTP返回的result中数据，建立一个模型对象
        注意： 调用此方法前要判断status是否为正确的状态,
        如果http返回的是400或500错误，就不要调用此方法。

        @param result: {"result": ...}
        @return: 模型对象
        """
        if isinstance(result, dict):
            result_dict = result
        else:
            result_dict = json.loads(result)
        result_data = result_dict.get('result', None)

        if result_data:
            data = result_data[0]
        else:
            data = result_dict

        return cls.from_primitive(data)

    @classmethod
    def from_multi_result(cls, result):
        """
        根据HTTP返回的result中数据，建立一个模型对象
        注意： 调用此方法前要判断status是否为正确的状态,
        如果http返回的是400或500错误，就不要调用此方法。

        @param result: {"result": ...}
        @return: 模型对象
        """
        result_dict = json.loads(result)
        result_data = result_dict.get('result', None)

        multi_datas = []
        if result_data:
            for data in result_data:
                multi_datas.append(cls.from_primitive(data))
        else:
            multi_datas = None

        return multi_datas