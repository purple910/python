"""
    @Time    : 2020/2/13 09:48
    @Author  : fate
    @Site    : 
    @File    : tvk2.py
    @Software: PyCharm
"""
from tvtk.api import tvtk

# 创建一个长方体数据源,设置其长宽高
s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
# 将数据源转换为图形数据
m = tvtk.PolyDataMapper(input_connection=s.output_port)
# 创建一个Actor
a = tvtk.Actor(mapper=m)
# 创建一个Renderer
r = tvtk.Renderer(background=(0, 0, 0))
r.add_actor(a)
# 创建一个窗口
w = tvtk.RenderWindow(size=(300, 300))
w.add_renderer(r)
# 创建一个窗口交互工具
i = tvtk.RenderWindowInteractor(render_window=w)
# 开启交互
i.initialize()
i.start()
