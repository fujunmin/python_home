# -*- coding: utf-8 -*-

#1.8  字典最大值，排序等
from collections import Counter

prices = {
    'ACME': 45.23,
    'AAPL' : 612.78,
    'IBM' : 205.55,
    'HPQ' : 37.20
}
def func1():
    min_price = min(zip(prices.values(),prices.keys()))
    # print min_price
    max_price = max(zip(prices.values(),prices.keys()))
    # print max_price

    #要实现排序，只要使用zip搭配sorted()即可
    sorted_prices = sorted(zip(prices.values(),prices.keys()))
    print sorted_prices

def use_zip():
    names = zip(prices.values(), prices.keys())
    print(min(names))
    print(max(names))

def func5():
    morewords = {'why','are','are'}
    word_count = Counter(morewords)
    # print word_count('are')
    top_three = word_count.most_common(2)
    print top_three
if __name__=='__main__':
    # use_zip()
    func5()

