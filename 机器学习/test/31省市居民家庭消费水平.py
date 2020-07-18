"""
    @Time    : 2020/2/16 15:01
    @Author  : fate
    @Site    : 
    @File    : 31省市居民家庭消费水平.py
    @Software: PyCharm
"""
'''
现有1999年全国31个省份城镇居民家庭平均每人全年消费性支出的八个主
要变量数据，这八个变量分别是：食品、 衣着、 家庭设备用品及服务、 医疗
保健、 交通和通讯、 娱乐教育文化服务、 居住以及杂项商品和服务。 利用已
有数据，对31个省份进行聚类。
'''

from sklearn.cluster import KMeans
import numpy as np


def loadData(filePath):
    fr = open(filePath, 'r+')
    lines = fr.readlines()
    retData = []
    retCityName = []
    for line in lines:
        items = line.strip().split(",")
        retCityName.append(items[0])
        retData.append([float(items[i]) for i in range(1, len(items))])
    return retData, retCityName


if __name__ == '__main__':
    data, cityName = loadData('课程数据/聚类/31省市居民家庭消费水平-city.txt')
    km = KMeans(n_clusters=4)
    label = km.fit_predict(data)
    expenses = np.sum(km.cluster_centers_, axis=1)
    # print(expenses)
    CityCluster = [[], [], [], []]
    for i in range(len(cityName)):
        CityCluster[label[i]].append(cityName[i])
    for i in range(len(CityCluster)):
        print("Expenses:%.2f" % expenses[i])
        print(CityCluster[i])
