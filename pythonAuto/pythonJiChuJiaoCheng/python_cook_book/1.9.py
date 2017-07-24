# -*- coding: utf-8 -*-

#1.9 找出两个字典的相同之处
a = {'x' : 1,'y' : 2,'z' :3  }
b = { 'x' : 11,'y' : 2,'w' : 10 }

#找出相同的key
def func1():
    a1 = a.viewkeys()
    b1 = b.viewkeys()
    compare = a1 & b1
    print compare   # set(['y','x'])
#a中有，b中没有的key
def func2():
    print a.viewkeys() - b.viewkeys()  #type:set

# 创建一个新的字典dict
def func3():
    c = {key:a[key]  for key in a.viewkeys() - {'x'}}
    print c



if __name__=='__main__':
    func3()


