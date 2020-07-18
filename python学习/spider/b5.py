import requests
from bs4 import BeautifulSoup
import re

try:
    url = "https://python123.io/ws/demo.html"
    r = requests.get(url)
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")

    # 搜索a标签,b标签
    for link in soup.find_all(name=['a', 'b']):
        print(link)

    # 搜索所有标签
    for link in soup.find_all(True):
        print(link.name)

    # 以b开头的标签
    for link in soup.find_all(re.compile('b')):
        print(link.name)

    # 查找p标签且有course属性的标签
    for link in soup.find_all(name='p', attrs='course'):
        print(link)

    # 字符串查找
    for link in soup.find_all(string=re.compile('python')):
        print(link)
except Exception as ex:
    print(ex)
