"""
    @Time    : 2020/2/14 09:20
    @Author  : fate
    @Site    : 
    @File    : mav1.py
    @Software: PyCharm
"""
from mayavi import mlab

x = [[-1, 1, 1, -1, -1], [-1, 1, 1, -1, -1]]
y = [[-1, -1, -1, -1, -1], [1, 1, 1, 1, 1]]
z = [[1, 1, -1, -1, 1], [1, 1, -1, -1, 1]]

s = mlab.mesh(x, y, z)
mlab.show()
