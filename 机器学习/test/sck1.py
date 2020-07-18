"""
    @Time    : 2020/2/16 13:39
    @Author  : fate
    @Site    : 
    @File    : sck1.py
    @Software: PyCharm
"""
from sklearn.datasets import load_digits, load_boston, load_iris
import matplotlib.pyplot as plt

boston = load_boston()
print(boston.data.shape)
data, target = load_boston(return_X_y=True)
print(data.shape)
print(target.shape)

iris = load_iris()
print(iris.data.shape)
print(iris.target.shape)
print(list(iris.target_names))

digits = load_digits()
print(digits.data.shape)
print(digits.target.shape)
print(digits.images.shape)

plt.matshow(digits.images[0])
plt.show()



