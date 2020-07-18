"""
    @Time    : 2020/2/14 10:38
    @Author  : fate
    @Site    : 
    @File    : mav4.py
    @Software: PyCharm
"""
import numpy as np
from mayavi import mlab

# 建立数据
t = np.linspace(0, 4 * np.pi, 20)  # linspace根据起止数据等间距填充数据，分为20组，所以下面将产生20个点
x = np.sin(2 * t)
y = np.cos(t)
z = np.cos(2 * t)
s = 2 + np.sin(t)

# 对数据进行可视化
# x,y,z表示Numpy数组，列表或者其他形式的点三维坐标，s表示在该点处的标量值，scale_factor放缩比例
points = mlab.points3d(x, y, z, s, colormap='Reds', scale_factor=.25)
mlab.show()
