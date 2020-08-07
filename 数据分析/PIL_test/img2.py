"""
    @Time    : 2020/8/5 14:29 
    @Author  : fate
    @Site    : 
    @File    : img2.py
    @Software: PyCharm
"""
from PIL import Image
import numpy as np

a = np.array(Image.open('a.jpg').convert('L'))
print(a.shape, a.dtype)

b = 255 - a
im = Image.fromarray(b.astype('uint8'))

im.save('2.jpg')
