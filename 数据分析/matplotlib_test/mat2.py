"""
    @Time    : 2020/8/5 15:05 
    @Author  : fate
    @Site    : 
    @File    : mat2.py
    @Software: PyCharm
"""
import matplotlib.pyplot as plt

plt.plot([0, 2, 4, 6, 8], [3, 1, 4, 5, 2])  # x y
plt.ylabel('grade')
plt.axis([-1, 10, 0, 6])    # -1<x<10 0<y<6
plt.show()
