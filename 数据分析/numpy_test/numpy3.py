"""
    @Time    : 2020/7/18 12:58
    @Author  : fate
    @Site    : 
    @File    : numpy3.py
    @Software: PyCharm
"""

import numpy as np

a = np.arange(24).reshape((2, 3, 4))
print(a)

print(a[1, 2, 3])
print(a[-1, -1, -1])
