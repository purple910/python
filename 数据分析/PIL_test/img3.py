"""
    @Time    : 2020/8/5 14:35 
    @Author  : fate
    @Site    : 
    @File    : img3.py
    @Software: PyCharm
"""
from PIL import Image
import numpy as np

a = np.array(Image.open('a.jpg').convert('L'))
print(a.shape, a.dtype)

b = 255 * (a / 255) ** 2
im = Image.fromarray(b.astype('uint8'))

im.save('3.jpg')
