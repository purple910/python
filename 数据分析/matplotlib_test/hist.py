"""
    @Time    : 2020/8/6 9:13 
    @Author  : fate
    @Site    : 
    @File    : hist.py
    @Software: PyCharm
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
mu, sigma = 100, 20  # 均值 标准差
a = np.random.normal(mu, sigma, size=100)
# print(a)

#   20 == 直方图的个数
plt.hist(a, 20, density=1, histtype='stepfilled', facecolor='b', alpha=0.75)
plt.title('Histogram')

plt.show()
