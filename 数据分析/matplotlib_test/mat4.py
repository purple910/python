"""
    @Time    : 2020/8/5 15:27 
    @Author  : fate
    @Site    : 
    @File    : mat4.py
    @Software: PyCharm
"""
import matplotlib.pyplot as plt
import numpy as np

a = np.arange(10)
plt.plot(a, a * 1.5, 'bo-', a, a * 2.5, '*', a, a * 3.5, 'rx', a, a * 4.5, 'g--_')  # x,y
plt.show()
