"""
    @Time    : 2020/2/14 15:49
    @Author  : fate
    @Site    : 
    @File    : mav9.py
    @Software: PyCharm
"""
import numpy as np
from mayavi import mlab

# ogrid返回3个三维数组（几个是不固定的，我们设置了几个元素，就生成相对应个三维数组）
x, y, z = np.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]    # 64j表示数组长度为64
print(x)
scalars = x * x + y * y + z * z
# contours八个等值面　　transparent该对象可以透明表示，可以查看内部
obj = mlab.contour3d(scalars, contours=8, transparent=True)
mlab.show()
