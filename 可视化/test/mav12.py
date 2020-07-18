"""
    @Time    : 2020/2/14 16:06
    @Author  : fate
    @Site    : 
    @File    : mav12.py
    @Software: PyCharm
"""
import numpy as np
from mayavi import mlab

x, y = np.mgrid[-10:10:200j, -10:10:200j]
z = 100*np.sin(x*y)/(x*y)

mlab.figure(bgcolor=(1, 1, 1))
surf = mlab.surf(z, colormap='cool')

# 访问surf对象LUT
# LUT是一个255*4的数组,列向量表示RGBA 0-255
lut = surf.module_manager.scalar_lut_manager.lut.table.to_array()
print(lut)

# 增加透明度
lut[:, -1] = np.linspace(0, 255, 256)
surf.module_manager.scalar_lut_manager.lut.table = lut

mlab.show()
