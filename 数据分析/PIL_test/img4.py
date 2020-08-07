"""
    @Time    : 2020/8/5 14:39 
    @Author  : fate
    @Site    : 
    @File    : img4.py
    @Software: PyCharm
"""
from PIL import Image
import numpy as np

a = np.array(Image.open('a.jpg').convert('L')).astype('float')

depth = 10.             # (0-100)
grad = np.gradient(a)   # 去图像的灰度的梯度值
grad_x, grad_y = grad   # 分别去图像的横纵梯度值
grad_x = grad_x * depth / 100
grad_y = grad_y * depth / 100
A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
uin_x = grad_x / A
uin_y = grad_y / A
uin_z = 1. / A

vec_e1 = np.pi / 2.2    # 光源的俯视角度,弧度值
vec_e2 = np.pi / 4.     # 光源的方向角度,弧度值
dx = np.cos(vec_e1) * np.cos(vec_e2)    # 光源对x的影响
dy = np.cos(vec_e1) * np.sin(vec_e2)    # 光源对y的影响
dz = np.sin(vec_e1)                     # 光源对z的影响

b = 255 * (dx * uin_x + dy * uin_y + dz * uin_z)    # 光源归一化
b = b.clip(0, 255)  # 为避免数据溢出,将灰度值剪切于0-255

im = Image.fromarray(b.astype('uint8'))     # 重构图像
im.save('4.jpg')
