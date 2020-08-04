"""
    @Time    : 2020/8/3 16:22 
    @Author  : fate
    @Site    : 
    @File    : npy.py
    @Software: PyCharm
"""
import numpy as np

a = np.arange(100).reshape((5, 10, 2))
np.save("a.npy", a)

b = np.load('a.npy')
print(b)
