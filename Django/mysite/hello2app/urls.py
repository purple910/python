"""
    @Time    : 2020/2/17 09:24
    @Author  : fate
    @Site    : 
    @File    : urls.py.py
    @Software: PyCharm
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello)
]
