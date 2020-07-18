"""
    @Time    : 2020/2/15 09:47
    @Author  : fate
    @Site    : 
    @File    : Quiver绘制.py
    @Software: PyCharm
"""
import numpy as np
from mayavi import mlab

x, y, z = np.mgrid[0:1:20j, 0:1:20j, 0:1:20j]
u = np.sin(np.pi * x) * np.cos(np.pi * z)
v = -2 * np.sin(np.pi * y) * np.cos(2 * np.pi * z)
w = np.cos(np.pi * x) * np.sin(np.pi * z) + np.cos(np.pi * y) * np.sin(2 * np.pi * z)

mlab.quiver3d(u, v, w)
mlab.outline()

mlab.show()
