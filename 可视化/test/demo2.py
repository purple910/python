"""
    @Time    : 2020/2/16 09:41
    @Author  : fate
    @Site    : 
    @File    : demo2.py
    @Software: PyCharm
"""
from traits.api import HasTraits, Instance, Range, on_trait_change
from traitsui.api import View, Item, Group
from mayavi.tools.mlab_scene_model import MlabSceneModel
# 引入视图编辑
from tvtk.pyface.scene_editor import SceneEditor
from mayavi.core.ui.mayavi_scene import MayaviScene
from mayavi.core.api import PipelineBase
# 数据产生
from numpy import arange, pi, cos, sin

dphi = pi / 300.
phi = arange(0.0, 2 * pi + 0.5 * dphi, dphi, 'd')


def curve(n_mer, n_long):
    mu = phi * n_mer
    x = cos(mu) * (1 + cos(n_long * mu / n_mer) * 0.5)
    y = sin(mu) * (1 + cos(n_long * mu / n_mer) * 0.5)
    z = 0.5 * sin(n_long * mu / n_mer)
    t = sin(mu)
    return x, y, z, t


class MyModel(HasTraits):
    n_meridional = Range(0, 36, 6)
    n_longitudinal = Range(0, 30, 11)
    scene = Instance(MlabSceneModel, ())

    plot = Instance(PipelineBase)

    @on_trait_change('n_meridional,n_longitudinal,scene.activated')
    def update_plot(self):
        x, y, z, t = curve(n_mer=self.n_meridional, n_long=self.n_longitudinal)
        if self.plot is None:
            self.plot = self.scene.mlab.plot3d(x, y, z, t,
                                               tube_radius=0.025, colormap='Spectral')
        else:
            self.plot.mlab_source.set(x=x, y=y, z=z, scalars=t)

    view = View(
        Item('scene', editor=SceneEditor(scene_class=MayaviScene),
             height=250, width=300, show_label=False),
        Group('_', 'n_meridional', 'n_longitudinal'),
        resizable=True
    )


model = MyModel()
model.configure_traits()
