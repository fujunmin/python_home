# -*- coding: utf-8 -*-



# 构造一个1, 3, 5, 7, ..., 99的列表

def func1():
    L = []
    n = 1
    while n <= 99:
        L.append(n)
        n = n + 2
    print L
#取一个list或tuple的部分元素是非常常见的操作
def func2():
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    r = []
    n = 3
    for i in range(n):
        r.append(L[i])
    print r

# 用一行代码解决切片问题
def func3():
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    print L[0:3]




if __name__=="__main__":
    func3()