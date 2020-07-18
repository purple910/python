"""
    @Time    : 2020/2/20 13:51
    @Author  : fate
    @Site    : 
    @File    : 手写数字_2.py
    @Software: PyCharm
"""
import numpy as np
from os import listdir
from sklearn import neighbors


def img2vector(filename):
    retMat = np.zeros([1024], int)
    fr = open(filename)
    lines = fr.readlines()
    for i in range(32):
        for j in range(32):
            retMat[i*32+j] = lines[i][j]
    return retMat


def readDataSet(path):
    fileList = listdir(path)
    numFiles = len(fileList)
    dataSet = np.zeros([numFiles, 1024], int)
    hwLabels = np.zeros([numFiles])
    for i in range(numFiles):
        filePath = fileList[i]
        digit = int(filePath.split('_')[0])
        hwLabels[i] = digit     # 直接存放数字
        dataSet[i] = img2vector(path + '/' + filePath)
    return dataSet, hwLabels


train_dataSet, train_hwLabels = readDataSet('课程数据/手写数字/digits/trainingDigits')

knn = neighbors.KNeighborsClassifier(algorithm='kd_tree', n_neighbors=3)
knn.fit(train_dataSet, train_hwLabels)

dataSet, hwLabels = readDataSet('课程数据/手写数字/digits/testDigits')

res = knn.predict(dataSet)
error_num = np.sum(res != hwLabels)
num = len(dataSet)

print('Total num:', num, '\nWrong num:', error_num, '\nWrongRate:', error_num / float(num))

