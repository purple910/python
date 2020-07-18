"""
    @Time    : 2020/2/19 09:20
    @Author  : fate
    @Site    : 
    @File    : 分类.py
    @Software: PyCharm
"""
import numpy as np
import pandas as pd
# 预处理器
from sklearn.impute import SimpleImputer
# 自动生成训练集和测试集
from sklearn.model_selection import train_test_split
# 预测结果评估模块
from sklearn.metrics import classification_report
'''分类器'''
# K进临分类器
from sklearn.neighbors import KNeighborsClassifier
# 决策树分类器
from sklearn.tree import DecisionTreeClassifier
# 高斯朴素贝叶斯函数
from sklearn.naive_bayes import GaussianNB


def load_dataset(feature_paths, label_paths):
    """读取特征文件列表和标签文件列表的内容"""
    feature = np.ndarray(shape=(0, 41))
    label = np.ndarray(shape=(0, 1))

    for file in feature_paths:
        # 使用逗号分隔符读取特征数, 将问号替换为缺失值, 文件不包含表头
        df = pd.read_table(file, delimiter=',', na_values='?', header=None)
        # 使用平均值补全缺失值, 将数据经行补全
        imp = SimpleImputer(missing_values=np.nan, strategy='mean')
        # print(df)
        # print(df.isnull().any())
        # print(imp)
        imp.fit(df)
        df = imp.transform(df)
        # 将型读入的数据合并到特征集合
        feature = np.concatenate((feature, df))

    for file in label_paths:
        # 读取标签数据, 不包含表头
        df = pd.read_table(file, header=None)
        # 将读取的数据合并到标签集合中
        label = np.concatenate((label, df))
    # 将标签归整为一维向量
    label = np.ravel(label)
    return feature, label


if __name__ == '__main__':
    feature_paths = ['课程数据\\分类\\dataset\\A\\A.feature',
                     '课程数据\\分类\\dataset\\B\\B.feature',
                     '课程数据\\分类\\dataset\\C\\C.feature',
                     '课程数据\\分类\\dataset\\D\\D.feature',
                     '课程数据\\分类\\dataset\\E\\E.feature']
    label_paths = ['课程数据\\分类\\dataset\\A\\A.label',
                   '课程数据\\分类\\dataset\\B\\B.label',
                   '课程数据\\分类\\dataset\\C\\C.label',
                   '课程数据\\分类\\dataset\\D\\D.label',
                   '课程数据\\分类\\dataset\\E\\E.label']
    # 将前四个数据作为训练数据读入
    x_train, y_train = load_dataset(feature_paths[:4], label_paths[:4])
    # 将后四个数据作为测试数据读入
    x_test, y_test = load_dataset(feature_paths[4:], label_paths[4:])
    # 使用全局数据作为训练集
    '''test_size：一般是是浮点数，在0-1之间，表示样本占比，比如test_size=0.2；如果是整数的话就是样本的数量；'''
    x_train, x_, y_train, y_ = train_test_split(x_train, y_train, test_size=0.1)

    #  创建K近邻分类器
    print("start training knn")
    knn = KNeighborsClassifier().fit(x_train, y_train)
    print("training done")
    answer_knn = knn.predict(x_test)
    print('prediction done')

    # 创建决策树分类器
    print('start training DT')
    dt = DecisionTreeClassifier().fit(x_train, y_train)
    print('training done')
    answer_dt = dt.predict(x_test)
    print('prediction done')

    # 创建贝叶斯分类器
    print('start training Bayes')
    gnb = GaussianNB().fit(x_train, y_train)
    print('training done')
    answer_gnb = gnb.predict(x_test)
    print('prediction done')

    # 计算精准率和召回率
    print("\n\nThe classification report for knn:")
    print(classification_report(y_test, answer_knn))
    print("\n\nThe classification report for dt:")
    print(classification_report(y_test, answer_dt))
    print("\n\nThe classification report for gnb:")
    print(classification_report(y_test, answer_gnb))

