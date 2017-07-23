# -*- coding: utf-8 -*-


'廖雪峰网站的python教程---函数的参数'


#可变参数
#请计算a2 + b2 + c2 + ……；由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来;
#调用的时候，需要先组装出一个list或tuple：
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print sum
    return sum

#把函数的参数改为可变参数
#在函数内部，参数numbers接收到的是一个tuple
def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print sum
    return sum

if __name__=="__main__":
    calc([1, 2, 3])
    calc((1, 3, 5, 7))  #调用的时候，需要先组装出一个list或tuple
    calc2()
    calc2(3,2)   #可以传入任意个参数，包括0个参数
    #  如果已经有一个list或者tuple，要调用一个可变参数怎么办
    nums = [1, 2, 3]
    calc2(*nums)   #Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去





