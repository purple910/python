"""
    @Time    : 2020/2/15 09:52
    @Author  : fate
    @Site    : 
    @File    : 级数的等值面.py
    @Software: PyCharm
"""
import numpy as np
from mayavi import mlab

x, y, z = np.mgrid[0:1:20j, 0:1:20j, 0:1:20j]
u = np.sin(np.pi * x) * np.cos(np.pi * z)
v = -2 * np.sin(np.pi * y) * np.cos(2 * np.pi * z)
w = np.cos(np.pi * x) * np.sin(np.pi * z) + np.cos(np.pi * y) * np.sin(2 * np.pi * z)

src = mlab.pipeline.vector_field(u, v, w)
magnitude = mlab.pipeline.extract_vector_norm(src)
mlab.pipeline.iso_surface(magnitude, contours=[2.0, 0.5])
mlab.outline()

mlab.show()
