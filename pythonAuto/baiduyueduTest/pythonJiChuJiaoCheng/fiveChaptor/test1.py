# -*- coding: UTF-8 -*-

#5.54 zip函数的用法
def zip_use():

    # 5.5.4
    names = ['anne','beth','george']
    ages = [12,33,32]
    print type(names)    #list
    # for i in range(len(names)):
    #     print names[i],'is',ages[i],'years old !'
#进行并行迭代，将两个序列“压缩”在一起，然后返回一个元组的列表
    for name,age in zip(names,ages):
        print name,'is',age,'years old !'
        print  zip(names,ages)


#5.54在一个字符串列表中替换所有包含‘xxx’的子字符串
def sezrchchild(strings):
    for string in strings:
        if 'xxx' in string:
            index = strings.index(string)
            strings[index] = '[censored'

#同上,搜索子字符串可以写成这样；当然也可以用内建的enumerate函数
def searchchild2(strings):
    index = 0
    for string in strings:
        if 'j' in string :
            strings[index] = 'censored'
        index += 1
        print strings

def  replace_string():
    strings = 'i love you baby'
    for string in strings:
        if 'baby' in string:
            index = strings.index(string)
            strings[index]='cerno'
            print strings
def test():
    print 'testgit'
def test2():
    print 'haha222333又修改了一次44'

if __name__ =='__main__':
    # replace_string()
    # zip_use()
    searchchild2("fujunmin")