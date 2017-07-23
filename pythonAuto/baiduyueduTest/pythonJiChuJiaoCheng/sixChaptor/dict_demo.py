# -*- coding: utf-8 -*-

# def savename1():
"""
storage这个数据结构存储了3个键，每个键下面又存储了一个字典，可以使用名字作为键，插入联系人列表作为值
比如要把我自己的名字加入到这个数据结构，可以

:return:
"""
# storage = {}
# storage['first'] = {}
# storage['middle'] = {}
# storage['last'] = {}
# me = 'Fu Jun min '
# storage['first']['min'] = me
# storage['middle']['Jun'] = me
# storage['last']['Fu'] = me

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
#编写存储名字函数之前，先编写一个获得名字的函数
def  lookup(data,label,name):
    if data[label].get(name) is not None:
        print  data[label].get(name)
    return data[label].get(name)

def storage(data,full_name):
    names = full_name.split()
    if len(names) ==2:  names.insert(1,' ')
    labels = 'first','middle','last'
    for label,name in zip(labels,names):
        people = lookup(data,label,name)
        # print people
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


if __name__=="__main__":
    # savename2()
    # lookup(storage,'first','11'
    mynames = {}
    init(mynames)
    storage(mynames,'wang zhi fei')
    # lookup(mynames,'middle','zhi')
    storage(mynames,'wang yi fan')
    lookup(mynames,'first','wang')