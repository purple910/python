"""
    @Time    : 2020/2/14 09:41
    @Author  : fate
    @Site    : 
    @File    : mav3.py
    @Software: PyCharm
"""
from numpy import pi, sin, cos, mgrid
from mayavi import mlab

dphi, dtheta = pi / 250.0, pi / 250.0
[phi, theta] = mgrid[0:pi + dphi * 1.5:dphi, 0:2 * pi + dtheta * 1.5:dtheta]
m0 = 4
m1 = 3
m2 = 2
m3 = 3
m4 = 6
m5 = 2
m6 = 6
m7 = 4

r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7
x = r*sin(phi)*cos(theta)
y = r*cos(phi)
z = r*sin(phi)*sin(theta)

# s = mlab.mesh(x, y, z, representation='wireframe', line_width=1.0)    # 线框
s = mlab.mesh(x, y, z)
# mlab.show()

# 获取场景对象
s = mlab.gcf()
print(s)
print(s.scene.background)

# 通过children属性, 在管线中找到需要修改的对象
source = s.children[0]
print(repr(source))
print(source.name)
print(repr(source.data.points))
print(repr(source.data.point_data.scalars))

# 一级一级的获取
manager = source.children[0]
print(manager)

# 设置颜色
colors = manager.children[0]
colors.scalar_lut_manager.lut_mode = 'Blues'
colors.scalar_lut_manager.show_legend = True

# 设置透明度
surface = colors.children[0]
surface.actor.property.representation = 'wireframe'
surface.actor.property.opacity = 0.7

mlab.show()
