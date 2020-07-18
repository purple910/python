import requests


def getHTMLText(url):
    try:
        r = requests.get(url=url, timeout=30)
        # 若返回值不是200 则异常
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "异常"


if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))
