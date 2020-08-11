"""
    @Time    : 2020/8/6 10:30 
    @Author  : fate
    @Site    : 
    @File    : pd1.py
    @Software: PyCharm
"""
import pandas as pd

a = pd.Series([9, 8, 7, 6, 5, 4])
print(a)

b = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
print(b)

c = pd.Series(22, index=['a', 'b', 'c'])
print(c)

d = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(d)

e = pd.Series({'a': 1, 'b': 2, 'c': 3}, index=['c', 'b', 'd', 'a'])
e.name = 'Series 对象'
e.index.name = '索引号'
print(e)

