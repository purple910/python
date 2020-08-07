"""
    @Time    : 2020/8/5 16:41 
    @Author  : fate
    @Site    : 
    @File    : mat7.py
    @Software: PyCharm
"""
import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0.0, 5.0, 0.02)

plt.ylabel('横轴', fontproperties='SimHei', fontsize=10)
plt.xlabel('纵轴', fontproperties='SimHei', fontsize=20)
plt.title(r'正弦波实例 $y=cos(2\pi x)$', fontproperties='SimHei', fontsize=33)
plt.text(2, 1, r'$\mu=100$', fontsize='15')
plt.axis([-1, 6, -2, 2])
plt.grid(True)
plt.plot(a, np.cos(2 * np.pi * a), 'r--')
plt.show()
