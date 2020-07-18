"""
    @Time    : 2020/2/15 18:16
    @Author  : fate
    @Site    : 
    @File    : tru5.py
    @Software: PyCharm
"""
from traits.api import Property, HasTraits, Float, cached_property, Int, Str, Event, on_trait_change
from traitsui.api import View, Item, Group, HSplit, VGroup

# View描述了界面的视图类，Item模块描述了界面中的控件类
g1 = [
    Item("model_name", label=u"模型名称"),
    Item("category", label=u"模型类型"),
]
g2 = [
    Item("model_number", label=u"模型数量"),
    Item("vertices", label=u"顶点数量"),
]


class ModelManager(HasTraits):
    model_name = Str
    category = Str
    model_number = Int
    vertices = Int

    traits_view = View(
        Group(*g1, label=u"模型信息", show_border=True),
        Group(*g2, label=u"统计数据", show_border=True),
        title=u"内部视图"
    )


global_view = View(
    Group(*g1, label=u"模型信息11", show_border=True),
    Group(*g2, label=u"统计数据11", show_border=True),
    title=u"外部视图"
)

model = ModelManager()
# model.configure_traits()    #默认是内部视图
# model.configure_traits(view="traits_view")  #有选择的选中某个内部视图
model.configure_traits(view=global_view)    #直接将外部视图赋给view
