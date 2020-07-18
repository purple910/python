import requests
from bs4 import BeautifulSoup

try:
    url = "https://python123.io/ws/demo.html"
    r = requests.get(url)
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")

    # 标题
    print(soup.title)

    # a标签 (第一个)
    print(soup.a)

    # a标签的父级标签
    print(soup.a.parent.name)

    # a标签的属性
    print(soup.a.attrs)
    print(soup.a.attrs['id'])

    # 类型
    print(type(soup.a.attrs))
    print(type(soup.a))

    # 内容
    print(soup.a.string)



except Exception as ex:
    print(ex)
