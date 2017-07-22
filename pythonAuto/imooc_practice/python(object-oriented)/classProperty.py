# -*- coding: utf-8 -*-

import requests
import  json

#python面向对象教程

class Programer(object):
    hobby = 'Play Computer'

    def __init__(self,name,age,weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        return self.__weight


if __name__=='__main__':
    programmer = Programer('Albert',25,80)
    # print dir(programmer)
    print programmer.__dict__   #obtained values from the  init function
    print programmer.get_weight()
    print programmer._Programer__weight  # this is output __weight's value

