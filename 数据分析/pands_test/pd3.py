"""
    @Time    : 2020/8/7 15:18 
    @Author  : fate
    @Site    : 
    @File    : pd3.py
    @Software: PyCharm
"""
import pandas as pd
import numpy as np

d = pd.DataFrame(np.arange(20).reshape(4, 5), index=['a', 'c', 'd', 'b'])
print(d)

i = d.sort_index()
print(i)
i = d.sort_index(ascending=False)
print(i)

n = d.sort_values(2, ascending=False)
print(n)

n = d.sort_values('a', axis=1, ascending=False)
print(n)

