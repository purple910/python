"""
    @Time    : 2020/2/15 10:05
    @Author  : fate
    @Site    : 
    @File    : Canyon地形可视化实例.py
    @Software: PyCharm
"""
import zipfile
import numpy as np
from mayavi import mlab

# https://dds.cr.usgs.gov/srtm/version2_1/SRTM1/Region_04/
hgt = zipfile.ZipFile("E:\\MyDownloads\\N36W113.hgt.zip").read("N36W113.hgt")

# 处理地形数据
data = np.fromstring(hgt, ">i2")  # 构建整数型数据，相当于2*8的16位数组
data.shape = (3601, 3601)  # 确定数组的行数和列数
data = data.astype(np.float32)  # 使用32位浮点型
data = data[:1000, 900:1900]  # 为了提高效率，我们只选取部分数据x:0-1000 y:900-1900
data[data == -32768] = data[data > 0].min()  # 数据中有-32768表示为空隙数据，将该数据设置为数据中的最小值

# 渲染地形hgt的数据data
mlab.figure(size=(400, 320), bgcolor=(0.16, 0.28, 0.46))  # 获取窗口，窗口大小为400，320
mlab.surf(data, colormap="gist_earth", warp_scale=0.2,
          vmin=1200, vmax=1610)

# 清空内存
del data
# 创建交互式可视化窗口
mlab.view(-5.9, 83, 570, [5.3, 20, 238])  # 设置相机的视角（可选）（方位角，高度，距离和焦点等）
mlab.show()
