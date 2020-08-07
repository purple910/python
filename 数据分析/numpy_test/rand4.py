"""
    @Time    : 2020/8/4 10:08 
    @Author  : fate
    @Site    : 
    @File    : rand4.py
    @Software: PyCharm
"""
import numpy as np

# 产生具有均匀分布的数组,low起始值,high结束值,size形状
uniform = np.random.uniform(0, 10, (3, 4))
print(uniform)

# 产生有正态分布的数组,loc均值,scale标准差,size形状
normal = np.random.normal(10, 5, (3, 4))
print(normal)

# 产生具有泊松分布的数组,lam随机事件概率,size形状
poisson = np.random.poisson(0.5, (3, 4))
print(poisson)
