# -*- coding: utf-8 -*-


'廖雪峰网站的python教程---函数的参数'


#关键字参数,关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw


if __name__=="__main__":
    person('Michael', 30)
    person('Bob', 35, city='Beijing')
    person('Adam', 45, gender='M', job='Engineer')
    #和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
    kw = {'city': 'Beijing', 'job': 'Engineer'}
    person('Jack', 24, city=kw['city'], job=kw['job'])   #这种调用方式可以简化写，如下面所示
    person('Jack', 24, **kw)


    



