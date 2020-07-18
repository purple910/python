"""
    @Time    : 2020/2/16 09:01
    @Author  : fate
    @Site    : 
    @File    : tru7.py
    @Software: PyCharm

                    Event属性             Trait属性
    触发监听事件      对Event属性赋值      值被改变后
    监听函数名       _event_fried()      _trait_changed()

"""

from traitsui.api import Item, Group, View
from traits.api import HasTraits, Str, Button, Int


class ButtonEditor(HasTraits):
    # 定义按钮
    my_button = Button('click me !!')
    counter = Int

    # 定义监听
    def _my_button_fired(self):
        self.counter += 1

    # 定义视图
    trait_view = View(
        'my_button',
        'counter',
        title='ButtonEditor',
        buttons=['ok', 'no'],
        resizable=True
    )


button = ButtonEditor()
button.configure_traits()
