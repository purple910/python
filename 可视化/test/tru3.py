"""
    @Time    : 2020/2/15 18:11
    @Author  : fate
    @Site    : 
    @File    : tru3.py
    @Software: PyCharm
"""

from traits.api import HasTraits, Str, Int
from traitsui.api import View, Item, HSplit,VGroup


class ModelManager(HasTraits):
    model_name = Str
    category = Str
    model_file = Str
    model_number = Int
    vertices = Int


view1 = View(
    HSplit(     # 大布局水平
        VGroup(     # 小布局内部垂直
            Item("model_name", label=u"模型名称"),
            Item("model_file", label=u"文件名"),
            Item("category", label=u"模型类型"),
            label=u"模型信息",
            show_border=True
        ),
        VGroup(
            Item("model_number", label=u"模型数量"),
            Item("vertices", label=u"顶点数量"),
            label=u"统计数据",
            show_border=True
        ),
        orientation="horizontal"
    )
)


model = ModelManager()
model.configure_traits(view=view1)
