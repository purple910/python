"""
    @Time    : 2020/2/13 20:16
    @Author  : fate
    @Site    : 
    @File    : tvk5.py
    @Software: PyCharm
"""

# 数据读取
from tvtk.api import tvtk
from tvtk_fun import ivtk_scene, event_loop

plot3d = tvtk.MultiBlockPLOT3DReader(
    xyz_file_name="combxyz.bin",
    q_file_name="combq.bin",
    scalar_function_number=100, vector_function_number=200
)  # 读入Plot3D数据
plot3d.update()  # 让plot3D计算其输出数据
grid = plot3d.output.get_block(0)  # 获取读入的数据集对象

# 创建等值面
con = tvtk.ContourFilter()  # 创建等值面对象
con.set_input_data(grid)
con.generate_values(10, grid.point_data.scalars.range)  # 指定轮廓数和数据范围

# 绘制数据
# 设定映射器的变量范围属性
m = tvtk.PolyDataMapper(scalar_range=grid.point_data.scalars.range,
                        input_connection=con.output_port)
a = tvtk.Actor(mapper=m)
a.property.opacity = 0.5  # 设定透明度为0.5
# 窗口绘制
win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()


