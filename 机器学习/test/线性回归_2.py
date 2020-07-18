"""
    @Time    : 2020/2/20 09:37
    @Author  : fate
    @Site    : 
    @File    : 线性回归_2.py
    @Software: PyCharm
"""
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

datasets_X = []
datasets_Y = []
fr = open('课程数据/回归/prices.txt', 'r')
lines = fr.readlines()

for line in lines:
    items = line.strip().split(',')
    datasets_X.append(int(items[0]))
    datasets_Y.append(int(items[1]))

length = len(datasets_X)
# 将元组转换为二维列数组
datasets_X = np.array(datasets_X).reshape([length, 1])
# 将元组转换为一维数组
datasets_Y = np.array(datasets_Y)

minX = min(datasets_X)
maxX = max(datasets_X)
X = np.arange(minX, maxX).reshape([-1, 1])

# 建立线性回归方程
poly_reg = PolynomialFeatures(degree=2)     # degree=2 表示建立datasets_X的二次多项式
X_poly = poly_reg.fit_transform(datasets_X)
lin_reg_2 = linear_model.LinearRegression()
lin_reg_2.fit(X_poly, datasets_Y)

# 查看线性回归系数
print('Coefficients:', lin_reg_2.coef_)
# 查看回归方程的截距
print('intercept:', lin_reg_2.intercept_)

# 可视化
plt.scatter(datasets_X, datasets_Y, color='red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()

