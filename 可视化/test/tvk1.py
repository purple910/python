"""
    @Time    : 2020/2/13 09:35
    @Author  : fate
    @Site    : 
    @File    : tvk1.py
    @Software: PyCharm
"""
from tvtk.api import tvtk


s = tvtk.CubeSource(x_length=1, y_length=2, z_length=3)
print(s)
print(s.x_length)
print(s.y_length)
print(s.z_length)
print(s.center)
print(s.output_points_precision)
