# -*- coding: utf-8 -*-

#1.17  筛选序列中的元素
from itertools import compress

mylist = [1, 4, 5, -3, -1]

#方法一：列表推导式
def func1():
    f1 = [n for n in mylist if n>0 and n<=4]
    print f1   #  [1,4]

#方法二：生成器表达式
def func2():
    mylist = [1,4,5,-3,-1]
    pos = (n  for n in mylist if n>0)
    print pos
    for x in pos :
        print(x)


#方法三：处理筛选逻辑的代码放到单独的函数中，然后使用内建的filter()函数处理

def func3():
    values = ['1','2','-3','-','N/A','5']
    def is_int(val):
        try:
            x = int(val)
            return  True
        except ValueError:
            return  False
    ivals = list(filter(is_int,values))
    print(ivals)   #['1', '2', '-3', '5']

#有一种筛选数据的情况是：不是丢弃掉旧的数据，而是用新值替换掉不满足条件的值
def func4 ():
    clip_neg = [n if n>0 else 0 for n in mylist ]
    print clip_neg
    clip_pos = [n if n<0 else 0 for n in mylist]
    print clip_pos

#itertools.compress用法:输入：可迭代对象以及一个不二选择器序列作为输入，
# 输出：给出所有在相应的布尔选择器中位True的可迭代对象元素
def func5():
    address =[
        'a 1',
        'b 2',
        'c 3',
        'd 4',
        'e 5'

    ]
    counts = [0,3,10,6,1]
    more5 = [n>5 for n in counts]
    # print more5
    address2 = list(compress(address,more5))
    print address2



if __name__=="__main__":
    func5()