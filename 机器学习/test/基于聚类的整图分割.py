"""
    @Time    : 2020/2/16 15:19
    @Author  : fate
    @Site    : 
    @File    : 基于聚类的整图分割.py
    @Software: PyCharm
"""
'''
目标：利用K-means聚类算法对图像像素点颜色进行聚类实现简单的图像分割
输出：同一聚类中的点使用相同颜色标记，不同聚类颜色不同
'''
import numpy as np
import PIL.Image as image
from sklearn.cluster import KMeans


def loadData(filePath):
    f = open(filePath, 'rb')
    data = []
    img = image.open(f)
    m, n = img.size
    for i in range(m):
        for j in range(n):
            x, y, z = img.getpixel((i, j))
            data.append([x / 256.0, y / 256.0, z / 256.0])
    f.close()
    return np.mat(data), m, n


imgData, row, col = loadData('课程数据/基于聚类的整图分割/bull.jpg')
label = KMeans(n_clusters=4).fit_predict(imgData)

label = label.reshape([row, col])
pic_new = image.new("L", (row, col))
for i in range(row):
    for j in range(col):
        pic_new.putpixel((i, j), int(256 / (label[i][j] + 1)))
pic_new.save("result-bull-4.jpg", "JPEG")
