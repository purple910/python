"""
    @Time    : 2020/2/20 10:11
    @Author  : fate
    @Site    : 
    @File    : 岭回归.py
    @Software: PyCharm
"""
from sklearn.linear_model import Ridge
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn import model_selection
import pandas as pd

data = pd.read_csv('课程数据\\回归\\岭回归.csv', encoding='UTF-8', parse_dates=[0], index_col=0)
# data.sort_index(0,ascending=True,inplace=True)

X = data.iloc[:, :4]  # 语法
y = data.iloc[:, 4]
poly = PolynomialFeatures(6)  # 设置多项式的最高次数
X = poly.fit_transform(X)
# 设置测试集的比例，random_state随机数种子
train_set_X, test_set_X, train_set_y, test_set_y = model_selection.train_test_split(X, y, test_size=0.3, random_state=0)

clf = Ridge(alpha=1.0, fit_intercept=True)
clf.fit(train_set_X, train_set_y)
clf.score(test_set_X, test_set_y)

# plot
start = 200
end = 300
y_pre = clf.predict(X)
time = np.arange(start, end)
plt.plot(time, y[start:end], 'b', label='real')
plt.plot(time, y_pre[start:end], 'r', label='predict')
plt.legend(loc='upper left')
plt.show()
