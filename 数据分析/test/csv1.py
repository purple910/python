"""
    @Time    : 2020/8/3 15:50 
    @Author  : fate
    @Site    : 
    @File    : csv1.py
    @Software: PyCharm
"""
import numpy as np

a = np.arange(100).reshape(5, 20)
np.savetxt("a.csv", a, fmt='%d', delimiter=',')
