"""
    @Time    : 2020/2/16 15:18
    @Author  : fate
    @Site    : 
    @File    : 学生月上网时间分布.py
    @Software: PyCharm
"""
'''
现有大学校园网的日志数据，290条大学生的校园网使用情况数据，数据包
括用户ID，设备的MAC地址，IP地址，开始上网时间，停止上网时间，上
网时长，校园网套餐等。 利用已有数据，分析学生上网的模式。
实验目的：
通过DBSCAN聚类，分析学生上网时间和上网时长的模式。

'''
import numpy as np
import sklearn.cluster as skc
from sklearn import metrics
import matplotlib.pyplot as plt

onlinetimes = {}
with open("课程数据/聚类/学生月上网时间分布-TestData.txt", encoding="utf8") as f:
    for line in f:
        info_list = line.strip().split(',')
        mac = info_list[2]
        onlinetime = int(info_list[6])
        # 获取上网的起始时候的小时 "2014-07-21 08:14:29.287000000" 这个的08
        starttime = int(info_list[4].split(' ')[1].split(':')[0])
        onlinetimes[mac] = (starttime, onlinetime)
real_X = np.array([onlinetimes[key] for key in onlinetimes]).reshape((-1, 2))
# 只获取上网的时间点
X = real_X[:, 0:1]

db = skc.DBSCAN(eps=0.01, min_samples=20).fit(X)
labels = db.labels_

# 获得噪声点比例
raito = len(labels[labels[:] == -1]) / len(labels)
print('Noise raito:', format(raito, '.2%'))

# 显示算法性能
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print('Estimated number of clusters: %d' % n_clusters_)
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels))

for i in range(n_clusters_):
    print('Cluster ', i, ':')
    print(list(X[labels == i].flatten()))

plt.hist(X, 24)
plt.show()
