"""
    @Time    : 2020/8/6 9:25 
    @Author  : fate
    @Site    : 
    @File    : subplot.py
    @Software: PyCharm
"""
import numpy as np
import matplotlib.pyplot as plt

N = 20      # 数据个数
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)  # 等分出20个数 每个18°
# print(theta)
radii = 10 * np.random.rand(N)      # 生成每个角度的长度值 r
# print(radii)
width = np.pi / 4 * np.random.rand(N)   # 生成角度 θ
# print(width)

ax = plt.subplot(111, projection='polar')   # 设置绘制极坐标
bars = ax.bar(theta, radii, width=width, bottom=0.0)    # left height width

for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))
    bar.set_alpha(0.5)

plt.show()
