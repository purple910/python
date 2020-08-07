"""
    @Time    : 2020/8/4 9:45 
    @Author  : fate
    @Site    : 
    @File    : rand2.py
    @Software: PyCharm
"""
import numpy as np

a = np.random.randint(100, 200, (3, 4))
print(a)

# 根据数组a的第一轴进行随机排序,改变数组a
np.random.shuffle(a)
print(a)

np.random.shuffle(a)
print(a)

# 根据数组a的第一轴产生一个新的乱序数组,不改变数组a
b = np.random.permutation(a)
print(b)
print(a)
