"""
    @Time    : 2020/2/14 15:44
    @Author  : fate
    @Site    : 
    @File    : mav7.py
    @Software: PyCharm
"""
import numpy as np
from mayavi import mlab


def f(x, y):
    return np.sin(x - y) + np.cos(x + y)


"""
mgrid返回两个二维数组（个数是不固定的，我们放置几个元素，就会生成几个二维数组）
-7.:7.05:0.1---->最小-7，最大7.05，步长为0.1依次生成一个n*n矩阵
"""
x, y = np.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
print(y)
s = mlab.surf(x, y, f)
mlab.show()
