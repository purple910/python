"""
    @Time    : 2020/2/15 10:06
    @Author  : fate
    @Site    : 
    @File    : 地球仪实例绘制.py
    @Software: PyCharm
"""
import numpy as np
from mayavi import mlab

# 城市经纬度数据
cities_data = """
Hong Kong,114.109497,114.109497
Miami,-80.19179,-80.19179
Manila,120.984219,120.984219
Caracas,-66.903606,-66.903606
Nicosia,33.382276,33.382276
Luxembourg,6.129583,6.129583
Mexico City,-99.133208,-99.133208
Doha,51.53104,51.53104
Prague,14.4378,14.4378
Delhi,77.209021,77.209021
Taipei,121.565418,121.565418
Tel Aviv,34.781768,34.781768
São Paulo,-46.633309,-46.633309
Oslo,10.752245,10.752245
Milan,9.185924,9.185924
Toronto,-79.383184,-79.383184
Helsinki,24.938379,24.938379
Chicago,-87.629798,-87.629798
Tokyo,139.691706,139.691706
Paris,2.352222,2.352222
Kuala Lumpur,101.686855,101.686855
Manama,50.58605,50.58605
Lyon,4.835659,4.835659
Madrid,-3.70379,-3.70379
Tallinn,24.753575,24.753575
Bucharest,26.102538,26.102538
Montreal,-73.567256,-73.567256
Riga,24.105186,24.105186
Istanbul,28.978359,28.978359
New York,-74.005941,-74.005941
Vilnius,25.279651,25.279651
Moscow,37.6173,37.6173
"""

# 1.建立城市-城索引的字典，城市经纬度的列表
import csv

cities = dict()
coords = list()
for line in list(csv.reader(cities_data.split("\n")))[1:-1]:  # 1:-1排除第一行只有一个\n
    name, long_, lat = line
    cities[name] = len(coords)  # 建立索引，len会随着coords增加而增加，这就是索引，我们根据这个去查找列表，更快
    coords.append((float(long_), float(lat)))

# 2.坐标转换
coords = np.array(coords)
lat, long = coords.T * np.pi / 180  # 进行转置
x = np.cos(long) * np.cos(lat)
y = np.cos(long) * np.sin(lat)
z = np.sin(long)

# 3.绘制窗口
mlab.figure(size=(400, 400), bgcolor=(0.48, 0.48, 0.48))

# 4.绘制球体mesh也可以，不过效果不好
sphere = mlab.points3d(  # 绘制半透明球体，表示地球外表面
    0, 0, 0,
    scale_factor=2,
    color=(0.67, 0.77, 0.93),
    resolution=50,
    opacity=0.7,
    name="Earth"
)

# 5.绘制城市名称
points = mlab.points3d(x, y, z,  # 已设置过的三维坐标
                       scale_mode="none",  # 放缩模式，标量，矢量，无
                       scale_factor=0.03,  # 放缩比例
                       color=(0, 0, 1))

# 6.绘制城市名字
for city, index in cities.items():
    label = mlab.text(x[index], y[index], city, z=z[index],  # x,y,city是城市名称，z坐标，width是文本宽度，name表示文本对象
                      width=0.016 * len(city), name=city)
    label.property.shadow = True

# 7.绘制地球上大洲的边界
from mayavi.sources.builtin_surface import BuiltinSurface

# 使用mlab的管线绘制表面函数对边界进行绘制
continents_src = BuiltinSurface(source="earth", name="Continents")
# 8.设置模型LOD的层级,实现近细远粗
continents_src.data_source.on_ratio = 2  # 2级lod
continents = mlab.pipeline.surface(continents_src, color=(0, 0, 0))

# 9.赤道线numpy数组的构造过程
theta = np.linspace(0, 2 * np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
z = np.zeros_like(theta)
# 10.绘制赤道线
mlab.plot3d(x, y, z, color=(1, 1, 1),
            opacity=0.2, tube_radius=None)

# 11.上面效果不是太好，添加镜面反射等参数
# 调整镜面反射参数
sphere.actor.property.specular = 0.45
sphere.actor.property.specular_power = 5
# 设置避免剔除，以更好的显示透明效果
sphere.actor.property.backface_culling = True

mlab.view(100, 60, 4, [-0.05, 0, 0])  # 设置相机的视角（可选）（方位角，高度，距离和焦点等）
mlab.show()
