# -*- coding: UTF-8 -*-


def zip_use():

    # 5.5.4
    names = ['anne','beth','george']
    ages = [12,33,32]
    print type(names)
    # for i in range(len(names)):
    #     print names[i],'is',ages[i],'years old !'

    for name,age in zip(names,ages):
        print name,'is',age,'years old !'

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
    replace_string()