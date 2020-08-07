"""
    @Time    : 2020/8/6 8:43 
    @Author  : fate
    @Site    : 
    @File    : mat9.py
    @Software: PyCharm
"""
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

gs = gridspec.GridSpec(3, 3)

# gs[行,列]
ax1 = plt.subplot(gs[0, :])
# ax2 = plt.subplot(gs[1, :-1])
ax2 = plt.subplot(gs[1, :2])
ax3 = plt.subplot(gs[1:, 2])
ax4 = plt.subplot(gs[2, 0])
ax5 = plt.subplot(gs[2, 1])

plt.show()
