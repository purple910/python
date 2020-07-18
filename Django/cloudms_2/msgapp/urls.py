"""
    @Time    : 2020/2/17 10:27
    @Author  : fate
    @Site    : 
    @File    : urls.py
    @Software: PyCharm
"""
from django.urls import path
from . import views

"""
    精确字符串:ars/1212/
    Django的转换:<类型:变量名>,ars/<int:year>/
    正则表达式:ars/(?P<year>[0-9]{4})/
"""

urlpatterns = [
    path('', views.msgproc),
]
