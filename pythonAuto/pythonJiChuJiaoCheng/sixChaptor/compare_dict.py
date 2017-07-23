# -*- coding: utf-8 -*-

# def bijiaodict(dict1, dict2):
#     for k, v in dict1.items():
#         for k2, v2 in dict2.items():
#             if k == k2 and v == v2:
#                 print('dict1=dict2')
#             else:
#                 print('dict1!=dict2')

# dict1 = {'2': '6'}
# dict2 = {2: {1: {1: 8}}}
# bijiaodict(dict1, dict2)


allGuests = {'Alice': {'apples': 5, 'pretzels': {'12':{'beijing':456}}},
             'Bob': {'ham sandwiches': 3, 'apple': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}
# print allGuests.items()

def dictget(dict1,obj,default=None):
    for k,v in dict1.items():
        if k == obj:
            print(v)
        else:
            if type(v) is dict:
                re=dictget(v,obj)
                if re is not default:
                    print(re)
# dictget(allGuests,'beijing')

def bianli(dict):
    for k,v in dict.items():
        print k
        print v

if __name__=="__main__":
    dictget(allGuests,'apples')
    # bianli(allGuests)
    print type(range(5))