import requests

url = "https://item.jd.com/100010658634.html"

try:
    r = requests.get(url=url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])

except Exception as ex:
    print("错误信息：%s" % ex)
