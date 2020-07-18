"""
    @Time    : 2020/2/15 9:30
    @Author  : fate
    @Site    : 
    @File    : 选择小球_2.py
    @Software: PyCharm
"""
from mayavi import mlab
import numpy as np

# 场景初始化
figure = mlab.gcf()
# 此时宣布绘制
figure.scene.disable_render = True

# 建立红色和白色小球的集合
x1, y1, z1 = np.random.random((3, 10))
red_glyphs = mlab.points3d(x1, y1, z1, color=(1, 0, 0), resolution=10)
x2, y2, z2 = np.random.random((3, 10))
white_glyphs = mlab.points3d(x2, y2, z2, color=(0.9, 0.9, 0.9), resolution=10)

# 绘制选取框,并放在第一个小丘上
outline = mlab.outline(line_width=3)
outline.outline_mode = 'cornered'
outline.bounds = (x1[0] - 0.1, x1[0] + 0.1,
                  y1[0] - 0.1, y1[0] + 0.1,
                  z1[0] - 0.1, z1[0] + 0.1)

# 此时开启绘制,将数据全部建立完成后统一绘制
figure.scene.disable_render = False
# 获取小球的顶点坐标
glyph_points = red_glyphs.glyph.glyph_source.glyph_source.output.points.to_array()


# 处理事件
def picker_callback(picker):
    if picker.actor in red_glyphs.actor.actors:
        # 计算那个小球被选中
        point_id = int(picker.point_id/glyph_points.shape[0])
        # 确定小球的id
        if point_id != -1:
            # 计算小球的坐标
            x, y, z = x1[point_id], y1[point_id], z1[point_id]
            # 将外框移动到小球上
            outline.bounds = (x - 0.1, x + 0.1,
                              y - 0.1, y + 0.1,
                              z - 0.1, z + 0.1)

    pass


# 建立相应机制
picker = figure.on_mouse_pick(picker_callback)
mlab.title('Click on red balls')
picker.tolerance = 0.01     # 提交选取精度
mlab.show()
