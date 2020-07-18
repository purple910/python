"""
    @Time    : 2020/2/14 15:40
    @Author  : fate
    @Site    : 
    @File    : mav6.py
    @Software: PyCharm
"""
from mayavi import mlab
import numpy as np

s = np.random.random((10, 10))  # 二维数据

img = mlab.imshow(s, colormap='gist_earth')  # gist_earth以地球表面的色彩为颜色的颜色映射关系
mlab.show()
