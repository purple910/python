"""
    @Time    : 2020/2/14 16:01
    @Author  : fate
    @Site    : 
    @File    : mav11.py
    @Software: PyCharm
"""
import numpy as np
from mayavi import mlab

x, y = np.mgrid[-10:10:200j, -10:10:200j]
z = 100*np.sin(x*y)/(x*y)

# 对数据进行可视化
mlab.figure(bgcolor=(1, 1, 1))
surf = mlab.surf(z, colormap='cool')    # cool 表示使用色系
mlab.show()
