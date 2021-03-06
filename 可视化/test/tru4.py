"""
    @Time    : 2020/2/15 18:05
    @Author  : fate
    @Site    : 
    @File    : tru4.py
    @Software: PyCharm
"""

from traits.api import HasTraits, Int, Str
from traitsui.api import View, Item, Group, ModalButtons


# View描述了界面的视图类，Item模块描述了界面中的控件类
class ModelManager(HasTraits):
    model_name = Str
    category = Str
    model_file = Str
    model_number = Int
    vertices = Int

    view1 = View(
        Group(
            Item("model_name", label=u"模型名称"),
            Item("model_file", label=u"文件名"),
            Item("category", label=u"模型类型"),
            label=u"模型信息",
            show_border=True
        ),
        Group(
            Item("model_number", label=u"模型数量"),
            Item("vertices", label=u"顶点数量"),
            label=u"统计数据",
            show_border=True
        ),
        kind="modal",
        buttons=ModalButtons
    )


model = ModelManager()
model.configure_traits()
