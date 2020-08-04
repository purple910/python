"""
    @Time    : 2020/8/3 15:57 
    @Author  : fate
    @Site    : 
    @File    : csv3.py
    @Software: PyCharm
"""
import numpy as np

a = np.loadtxt("b.csv", delimiter=",")
print(a)

b = np.loadtxt("b.csv", dtype=np.int, delimiter=",")
print(b)
