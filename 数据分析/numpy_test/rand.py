"""
    @Time    : 2020/8/4 9:37 
    @Author  : fate
    @Site    : 
    @File    : rand.py
    @Software: PyCharm
"""
import numpy as np

b = np.random.randn(3, 4, 5)
print(b)

a = np.random.randint(100, 200, (3, 4))
print(a)
