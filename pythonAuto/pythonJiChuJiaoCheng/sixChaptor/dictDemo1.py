# -*- coding: utf-8 -*-
people={
    'Alice':{
        'phone':'2341',
        'addr':'Foo drive 23'
    }
}

labels={
    'phone':'phone number',
    'addr':'address'
}

name=input('Name: ')
if name in people :
    print('名称存在')
else:
    print('名字输入有误')
request=input('Phone number(p) or address (a)?')
if request == 'p' : key='phone'
if request=='a' : key= 'addr'

if name in people : print("%s's %s is %s" %(name,labels[key],people[name][key]))







