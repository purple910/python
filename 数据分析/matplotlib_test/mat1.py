"""
    @Time    : 2020/8/5 14:59 
    @Author  : fate
    @Site    : 
    @File    : mat1.py
    @Software: PyCharm
"""
import matplotlib.pyplot as plt

plt.plot([3, 1, 4, 5, 2])  # (1,3) (2,1) (3,4) (4,5) (5,2)
plt.ylabel('grade')
plt.savefig('test', dpi=600)    # png
plt.show()
