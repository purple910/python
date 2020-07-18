"""
    @Time    : 2020/2/19 19:57
    @Author  : fate
    @Site    : 
    @File    : 分类_股票.py
    @Software: PyCharm
"""
import time
import pandas as pd
import numpy as np
from sklearn import svm     # svm算法
from sklearn import model_selection     # 交叉验证注：前面版本用cross_vallidation

# 数据加载与预处理
data = pd.read_csv('课程数据\\分类\\stock\\000777.csv', encoding='GBK', parse_dates=[0], index_col=0)
# 将data数据按照行索引顺序进行排列，从小到大
data.sort_index(0, ascending=True, inplace=True)

# 这里选取5列数据为特征：收盘价，最高价，最低价，开盘价，成交量
dayfeature = 150
featurenum = 5 * dayfeature
x = np.zeros((data.shape[0]-dayfeature, featurenum+1))
y = np.zeros((data.shape[0]-dayfeature))

# 将数据中的“收盘价”“最高价”“开盘价”“最低价”“成交量”存入x
# 数组中
for i in range(0, data.shape[0] - dayfeature):
    x[i, 0:featurenum] = np.array(data[i:i + dayfeature]
                                      [[u'收盘价', u'最高价', u'最低价', u'开盘价', u'成交量']]).reshape((1, featurenum))
    x[i, featurenum] = data.iloc[i + dayfeature][u'开盘价']  # 最后一列记录当日的开盘价

for i in range(0, data.shape[0] - dayfeature):
    if data.iloc[i + dayfeature][u'收盘价'] >= data.iloc[i + dayfeature][u'开盘价']:
        y[i] = 1
    else:
        y[i] = 0

# 如果当天收盘价高于开盘价，y[i]=1代表涨，0代表跌
clf = svm.SVC(kernel='rbf')   # 调用 svm 函数 ，并设置 kernel参数 ，默认是 rbf ，其它：linear poly sigmoid
# process_time()不包括sleep()休眠时间期间经过的时间
# perf_counter()会包含sleep()休眠时间，适用测量短持续时间
# start = time.perf_counter()
start = time.process_time()
result = []
for i in range(5):
    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)
    # x和y的验证集和测试集，切片80—20%的测试集
    clf.fit(x_train, y_train)
    # 训练数据进行训练
    result.append(np.mean(y_test == clf.predict(x_test)))
# 将预测数据和测试集的验证数据比对
print("svm classifier accuacy:")
print(result)
end = time.process_time()
print("running time %s Seconds" % (end-start))
