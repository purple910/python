"""
    @Time    : 2020/8/6 8:56 
    @Author  : fate
    @Site    : 
    @File    : pie.py
    @Software: PyCharm
"""
import matplotlib.pyplot as plt

label = 'Frogs', 'Hogs', 'Dogs', 'Logs'
size = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)

plt.pie(size, explode, labels=label, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')

plt.show()
