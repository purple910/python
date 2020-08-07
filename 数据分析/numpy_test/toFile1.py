"""
    @Time    : 2020/8/3 16:01 
    @Author  : fate
    @Site    : 多维数据储存
    @File    : toFile1.py
    @Software: PyCharm
"""
import numpy as np

a = np.arange(100).reshape(5, 10, 2)
a.tofile("a.dat", sep=",", format='%d')

b = np.fromfile("a.dat", dtype=np.int, sep=",")
print(b)

c = np.fromfile('a.dat', dtype=np.int, sep=",").reshape(5, 10, 2)
print(c)
