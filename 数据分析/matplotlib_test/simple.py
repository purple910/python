"""
    @Time    : 2020/8/6 10:11 
    @Author  : fate
    @Site    : 
    @File    : simple.py
    @Software: PyCharm
"""
import numpy as np
import matplotlib.pyplot as plt

flg, ax = plt.subplots()
ax.plot(10 * np.random.randn(100), 10 * np.random.randn(100), 'o')
ax.set_title('Simple Scatter')

plt.show()
