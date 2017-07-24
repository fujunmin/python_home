# -*- coding: utf-8 -*-

#1.17  从字典中提取子集

prices = {
    'ACME': 45.23,
    'AAPL' : 612.78,
    'IBM' : 205.55,
    'HPQ' : 37.20
}

# prices2 =
for key in prices.keys():
    key.strip('')
    print key

p1 = { key:value for key,value in prices.items() if value >200 }
# print p1

tech_names = { 'AAPL','IBM','HPQ','MSFT'}
p2 = { key:value for key,value in prices.items() if key in tech_names}
print  p2


