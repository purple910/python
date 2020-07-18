import requests
from bs4 import BeautifulSoup

try:
    url = "https://python123.io/ws/demo.html"
    r = requests.get(url)
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    # print(soup.prettify())

    print(soup.a.prettify())

except Exception as ex:
    print(ex)
