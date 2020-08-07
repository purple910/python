"""
    @Time    : 2020/8/5 14:22 
    @Author  : fate
    @Site    : 
    @File    : img1.py
    @Software: PyCharm
"""
from PIL import Image
import numpy as np

a = np.array(Image.open('a.jpg'))
print(a.shape, a.dtype)

b = [255, 255, 255] - a
im = Image.fromarray(b.astype('uint8'))

im.save('1.jpg')
