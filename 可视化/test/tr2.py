"""
    @Time    : 2020/2/15 14:40
    @Author  : fate
    @Site    : 
    @File    : tr2.py
    @Software: PyCharm
"""
from traits.api import HasTraits, Color, Delegate, Instance, Int, Str


class Child(HasTraits):
    name = Str
    age = Int
    doing = Str

    def __str__(self):
        return "%s<%x>" % (self.name, id(self))

    # 静态监听age属性的变化
    def _age_changed(self, old, new):
        print("%s.age changed: from %s to %s" % (self, old, new))

    # 静态监听trait的变化
    def _anytrait_changed(self, name, old, new):
        print("anytrait changed: %s.%s from %s to %s" % (self, name, old, new))


def log_trait_chenged(obj, name, old, new):
    print("log: %s.%s changed from %s to %s" % (obj, name, old, new))


z = Child(name='ZhangSan', age=4)
l = Child(name='LiSi', age=1)

# 动态监听doing属性的变化
z.on_trait_change(log_trait_chenged, name='doing')
z.doing = 'playing'
l.doing = 'playing'
