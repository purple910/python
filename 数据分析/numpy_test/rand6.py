"""
    @Time    : 2020/8/4 10:31 
    @Author  : fate
    @Site    : 
    @File    : rand6.py
    @Software: PyCharm
"""
import numpy as np

b = np.arange(15, 0, -1).reshape(3, 5)
print(b)

# 最大值,最小值
print(np.max(b))
print(np.min(b))

# 最大值,最小值的降一维后的下标
print(np.argmax(b))
print(np.argmin(b))

# 根据shape将一维下标index转换为多维下标
print(np.unravel_index(np.argmax(b), b.shape))

# 最大值与最小值的差
print(np.ptp(b))

# 中位值
print(np.median(b))
