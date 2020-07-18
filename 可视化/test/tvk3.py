"""
    @Time    : 2020/2/13 10:23
    @Author  : fate
    @Site    : 
    @File    : tvk3.py
    @Software: PyCharm
"""
from tvtk.api import tvtk

img = tvtk.ImageData(spacing=(1, 1, 1,), origin=(1, 2, 3), dimensions=(3, 4, 5))
for i in range(9):
    print(img.get_point(i))



