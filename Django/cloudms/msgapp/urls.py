from . import views
from django.urls import path

"""
    精确字符串:ars/1212/
    Django的转换:<类型:变量名>,ars/<int:year>/
    正则表达式:ars/(?P<year>[0-9]{4})/
"""

urlpatterns = [
    path('', views.msgproc),
]
