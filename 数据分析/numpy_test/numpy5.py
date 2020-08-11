"""
    @Time    : 2020/8/10 14:00 
    @Author  : fate
    @Site    : 
    @File    : numpy5.py
    @Software: PyCharm
"""
import numpy as np

a = np.arange(16).reshape(4, 4)
print(a)
b = np.arange(16).reshape(4, 4)
print(b)

# print(np.stack((a, b), 0))  # 添加一个新的维度
# print(np.vstack((a, b)))  # 竖直方向添加
# print(np.hstack((a, b)))  # 水平方向添加

print(np.hsplit(a, 2))  # 水平方向拆分为等份
print(np.hsplit(a, (1, 2)))  # 从那个下标开始拆分
print(np.vsplit(a, 2))  # 垂直方向拆分为等份
print(np.vsplit(a, (1, 2)))  # 从那个下标开始拆分
print(np.split(a, 2, axis=1))   # 自定义拆分维度
