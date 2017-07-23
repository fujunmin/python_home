# -*- coding: utf-8 -*-


'廖雪峰网站的python教程---函数的参数'


#默认参数,默认是求平方，也可以求三次方   power(5,3)
"""一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
二是如何设置默认参数。
当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数"""
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    print s
    return s
#默认参数可以指定，也可以不指定，如果不指定，就使用默认的参数值
def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

#默认参数的坑：默认参数必须指向不变对象！！！
def add_end(L=[]):
    L.append('END')
    print L
    return L

#对上面函数的补充完善，现在，无论调用多少次，都不会有问题
def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    print L
    return L

if __name__=="__main__":
    # power(5,3)
    # enroll('fjm','women',age =22, city='hangzhou')
    # enroll('Bob', 'M', 7)
    add_end()
    add_end()  #add_end()连续调用两次，输出结果却成了 ['END', 'END']
    add_end2()
    add_end2()

