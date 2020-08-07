"""
    @Time    : 2020/8/3 15:33 
    @Author  : fate
    @Site    : 
    @File    : numpy4.py
    @Software: PyCharm
"""
import numpy as np

a = np.arange(24).reshape((2, 3, 4))
print(a)
print(a.mean())  # 平均值
print(a / a.mean())
print(np.square(a))
print(np.sqrt(a))
print(np.maximum(a, np.sqrt(a)))
print(a > np.sqrt(a))
