"""
    @Time    : 2020/8/5 16:33 
    @Author  : fate
    @Site    : 
    @File    : mat6.py
    @Software: PyCharm
"""
import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0.0, 5.0, 0.02)

plt.ylabel('横轴', fontproperties='SimHei', fontsize=10)
plt.xlabel('纵轴', fontproperties='SimHei', fontsize=20)
plt.plot(a, np.cos(2 * np.pi * a), 'r--')
plt.show()
