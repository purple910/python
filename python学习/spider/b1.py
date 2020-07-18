import requests
from bs4 import BeautifulSoup

try:
    url = "https://python123.io/ws/demo.html"
    r = requests.get(url)
    demo = r.text
    print(demo)
    print()

    # 自动将html格式化
    soup = BeautifulSoup(demo, "html.parser")
    print(soup.prettify())
except Exception as ex:
    print(ex)
