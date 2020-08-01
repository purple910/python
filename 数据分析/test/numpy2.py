"""
    @Time    : 2020/7/18 12:45
    @Author  : fate
    @Site    : 
    @File    : numpy2.py
    @Software: PyCharm
"""
import numpy as np

a = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
])

b = np.array([
    [[0, 1], [2, 3]],
    [[4, 5], [6, 7]],
    [[8, 9], [10, 11]]
])

c = np.array([
    [0, 1, 2, 3],
    [4, 5, 6, 7, 8, 9]
])

# 秩
print(a.ndim)
print(b.ndim)
print(c.ndim)
# 尺度,n行m列
print(a.shape)
print(b.shape)
print(c.shape)
# 个数
print(a.size)
print(b.size)
print(c.size)
# 类型
print(a.dtype)
print(b.dtype)
print(c.dtype)
# 每个元素的大小
print(a.itemsize)
print(b.itemsize)
print(c.itemsize)
