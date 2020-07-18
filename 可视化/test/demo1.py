"""
    @Time    : 2020/2/16 09:19
    @Author  : fate
    @Site    : 
    @File    : demo1.py
    @Software: PyCharm
"""
from traits.api import HasTraits, Instance
from traitsui.api import View, Item
from mayavi.tools.mlab_scene_model import MlabSceneModel
# 引入视图编辑
from tvtk.pyface.scene_editor import SceneEditor
from mayavi.core.ui.mayavi_scene import MayaviScene
# 数据产生
from numpy import sqrt, sin, mgrid


# 建立traits的继承类
class ActorViewer(HasTraits):
    # 建立场景实例
    scene = Instance(MlabSceneModel, ())

    # 提供mayavi试图窗口
    view = View(
        Item(name='scene',
             editor=SceneEditor(scene_class=MayaviScene),
             show_label=False,
             resizable=True,
             height=500,
             width=500
             ),
        resizable=True
    )

    # 重载初始化函数
    def __init__(self, **tratis):
        HasTraits.__init__(self, **tratis)
        self.generate_data()

    #
    def generate_data(self):
        # 建立数据
        X, Y = mgrid[-2:2:100j, -2:2:100j]
        R = 10 * sqrt(X**2+Y**2)
        Z = sin(R)/R
        # 绘制数据
        self.scene.mlab.surf(X, Y, Z, colormap='cool')


# 显示窗口
a = ActorViewer()
a.configure_traits()

