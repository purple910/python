"""
    @Time    : 2020/2/15 18:26
    @Author  : fate
    @Site    : 
    @File    : tru6.py
    @Software: PyCharm
"""
from traitsui.api import Item, Group, View
from traits.api import HasTraits, Str, Password


class TextEditor(HasTraits):
    string_trait = Str('sample string')
    password = Password

    text_str_group = Group(
        Item('string_trait', style='simple', label='Simple'),
        Item('_'),
        Item('string_trait', style='custom', label='Custom'),
        Item('_'),
        Item('password', style='simple', label='password'),
    )

    traits_view = View(
        text_str_group,
        title='TextEditor',
        buttons=['ok']
    )


text = TextEditor()
text.configure_traits()
