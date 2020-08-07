"""
    @Time    : 2020/8/4 10:17 
    @Author  : fate
    @Site    : 
    @File    : rand5.py
    @Software: PyCharm
"""
import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)

# 求和
print(np.sum(a))
# 期望
print(np.mean(a, axis=1))
print(np.mean(a, axis=0))
# 加权平均值
print(np.average(a, axis=0, weights=[10, 5, 1]))
# 标准差
print(np.std(a))
# 方差
print(np.var(a))
