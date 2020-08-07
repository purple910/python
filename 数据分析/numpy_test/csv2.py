"""
    @Time    : 2020/8/3 15:53 
    @Author  : fate
    @Site    : 
    @File    : csv2.py
    @Software: PyCharm
"""
import numpy as np

a = np.arange(100).reshape(5, 20)
np.savetxt("b.csv", a, "%.1f", delimiter=",")
