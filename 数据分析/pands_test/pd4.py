"""
    @Time    : 2020/8/13 11:29 
    @Author  : fate
    @Site    : 
    @File    : pd4.py
    @Software: PyCharm
"""
import pandas as pd
import numpy as np

# df = pd.DataFrame(np.arange(16).reshape(4, 4), columns=['A', 'B', 'C', 'D'])
# print(df)
# print(type(df))

# print(df.apply(lambda x: x ** 2))
# print(df.transform(lambda x: x ** 2))
# print(df.agg(lambda a: a ** 2))
# print(df.apply(lambda x: x[1] * x[2], axis=1))
# print(df.transform(np.sum))
# print(df.agg(np.sum))


series = pd.Series(np.arange(4))
print(series)
print(type(series))
print(series.transform(np.sum))
