import requests
from bs4 import BeautifulSoup

try:
    url = "https://python123.io/ws/demo.html"
    r = requests.get(url)
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")

    print(soup.head.contents)
    print(soup.body.contents)

    print(len(soup.body.contents))

    for child in soup.body.children:
        print(child)

    # a标签的平行标签 可以是字符串
    print(soup.a.next_sibling)
    print(soup.a.next_sibling.next_sibling)

    # previous_siblings 之前所用的标签
    print(soup.a.previous_siblings)


except Exception as ex:
    print(ex)
