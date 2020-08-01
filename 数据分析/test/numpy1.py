"""
    @Time    : 2020/2/22 10:49
    @Author  : fate
    @Site    : 
    @File    : numpy1.py
    @Software: PyCharm
"""
# A*A+B*B*B
import numpy as np


def pySum():
    a = [0, 1, 2, 3, 4]
    b = [9, 8, 7, 6, 5]
    c = []

    for i in range(len(a)):
        c.append(a[i] ** 2 + b[i] ** 3)

    return c


s = pySum()
print(s)


def npSum():
    a = np.array([0, 1, 2, 3, 4])
    b = np.array([9, 8, 7, 6, 5])
    c = a ** 2 + b ** 3
    return c


s = npSum()
print(s)

