"""
    @Time    : 2020/8/7 14:38 
    @Author  : fate
    @Site    : 
    @File    : pd2.py
    @Software: PyCharm
"""
import pandas as pd
import numpy as np

d = pd.DataFrame(np.arange(10).reshape(2, 5))
print(d)

dt = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
}
d = pd.DataFrame(dt)
print(d)

d = pd.DataFrame(dt, index=['b', 'c', 'a'], columns=['three', 'two'])
print(d)

dl = {'one': [1, 2, 3], 'two': [9, 8, 7]}
d = pd.DataFrame(dl, index=['a', 'b', 'c'])
print(d)

