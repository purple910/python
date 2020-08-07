"""
    @Time    : 2020/8/5 15:09 
    @Author  : fate
    @Site    : 
    @File    : mat3.py
    @Software: PyCharm
"""
import matplotlib.pyplot as plt
import numpy as np


def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


a = np.arange(0.0, 5.0, 0.002)

plt.subplot(211)  # 2行 1列 第1各区域
plt.plot(a, f(a))

plt.subplot(2, 1, 2)
plt.plot(a, np.cos(2 * np.pi * a), 'r--')
plt.show()
