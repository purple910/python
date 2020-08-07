"""
    @Time    : 2020/8/5 15:42 
    @Author  : fate
    @Site    : 
    @File    : mat5.py
    @Software: PyCharm
"""
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.style'] = 'italic'
matplotlib.rcParams['font.size'] = 15
plt.plot([3, 1, 4, 5, 2])
plt.ylabel("纵轴")
plt.savefig('test1', dpi=600)
plt.show()
