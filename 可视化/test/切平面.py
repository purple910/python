"""
    @Time    : 2020/2/15 09:41
    @Author  : fate
    @Site    : 
    @File    : 切平面.py
    @Software: PyCharm
"""
import numpy as np
from mayavi import mlab

x, y, z = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
s = np.sin(x*y*z)/(x*y*z)

mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s),  # 数据的标量数据场
                                 plane_orientation='x_axes',  # 切平面的方向
                                 slice_index=10
                                 )
mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s),
                                 plane_orientation='y_axes',
                                 slice_index=10
                                 )
mlab.outline()
mlab.show()
