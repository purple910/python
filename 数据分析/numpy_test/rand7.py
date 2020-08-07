"""
    @Time    : 2020/8/4 10:42 
    @Author  : fate
    @Site    : 
    @File    : rand7.py
    @Software: PyCharm
"""
import numpy as np

a = np.random.randint(0, 20, 5)
print(a)

# 计算数组f中元素的梯度,当f为多维时,返回每个维度的梯度
print(np.gradient(a))

b = np.random.randint(0, 50, (3, 5))
print(b)

print(np.gradient(b))
