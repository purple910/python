"""
    @Time    : 2020/2/20 10:27
    @Author  : fate
    @Site    : 
    @File    : 手写数字.py
    @Software: PyCharm
"""
import numpy as np
from os import listdir
from sklearn.neural_network import MLPClassifier


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
    hwLabels = np.zeros([numFiles, 10])
    for i in range(numFiles):
        filePath = fileList[i]
        digit = int(filePath.split('_')[0])
        hwLabels[i][digit] = 1.0
        dataSet[i] = img2vector(path + '/' + filePath)
    return dataSet, hwLabels


train_dataSet, train_hwLabels = readDataSet('课程数据/手写数字/digits/trainingDigits')

clf = MLPClassifier(hidden_layer_sizes=(100,),
                    activation='logistic', solver='adam',
                    learning_rate_init=0.0001, max_iter=2000)
clf.fit(train_dataSet, train_hwLabels)

dataSet, hwLabels = readDataSet('课程数据/手写数字/digits/testDigits')

res = clf.predict(dataSet)
error_num = 0
num = len(dataSet)
for i in range(num):
    if np.sum(res[i] == hwLabels[i]) < 10:
        error_num += 1

print('Total num:', num, '\nWrong num:', error_num, '\nWrongRate:', error_num / float(num))
