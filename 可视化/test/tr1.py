"""
    @Time    : 2020/2/15 10:35
    @Author  : fate
    @Site    : 
    @File    : tr1.py
    @Software: PyCharm
"""
from traits.api import HasTraits, Color, Delegate, Instance, Int, Str


class Parent(HasTraits):
    # 初始化
    last_name = Str('zhang')


class Child(HasTraits):
    age = Int
    # 验证
    father = Instance(Parent)
    # 代理
    last_name = Delegate('father')

    # 监听
    def _age_changed(self, old, new):
        print('age change from %s to %s' % (old, new))


p = Parent()
c = Child()
c.father = p

print(c.last_name)

c.age = 4

# c.configure_traits()
c.print_traits()
# c.get()
