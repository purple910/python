"""
    @Time    : 2020/8/4 9:53 
    @Author  : fate
    @Site    : 
    @File    : rand3.py
    @Software: PyCharm
"""
import numpy as np

b = np.random.randint(100, 200, (8,))

# 从一维数组a中一概率p抽取元素,形成size形状新数组,replace表示是否可以重用元素,默认可以重用
choice = np.random.choice(b, (3, 2))
print(choice)

choice = np.random.choice(b, (3, 2), replace=False)
print(choice)

choice = np.random.choice(b, (3, 2), p=b / np.sum(b))
print(choice)
