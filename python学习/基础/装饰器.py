"""
    @Time    : 2020/8/7 15:18 
    @Author  : fate
    @Site    : 
    @File    : 装饰器.py
    @Software: PyCharm
"""
import time

import pandas as pd

from functools import wraps


def a_new_decorator(a_func):
    # 如果没有则wrapTheFunction
    # 我们调用的是a_function_requiring_decoration,但实际上运行的是wrapTheFunction
    # 为了避免它重写了我们函数的名字和注释文档
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")


print(a_function_requiring_decoration.__name__)


class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decorator runing')
        self._func()
        print('class decorator ending')


@Foo
def bar():
    print('bar')


bar()