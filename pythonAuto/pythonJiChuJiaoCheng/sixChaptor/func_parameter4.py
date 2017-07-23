# -*- coding: utf-8 -*-


'廖雪峰网站的python教程---函数的参数'


#参数组合讲解
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw


if __name__=="__main__":
    func(1, 2)
    func(1, 2, c=3)
    func(1, 2, 3, 'a', 'b')
    func(1, 2, 3, 'a', 'b','aabb', x=99)  #可变参数*args接收的是可变多个参数，在接收参数时会将其组装成tuple；关键字参数**kw会将接收参数组装成dict
    args = (5, 6, 7)
    kw = {'x': 99}
    func(*args, **kw)  #需要引起注意


    



