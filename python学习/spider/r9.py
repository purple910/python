import requests

url = "https://www.amazon.cn/dp/B07PDZG1QV"

try:
    # print(r.request.headers)
    # 'User-Agent': 'python-requests/2.22.0'
    # 更改请求头信息
    kv = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url=url, headers=kv)

    # r = requests.get(url=url)
    print(r.status_code)
    print(r.request.headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])

except Exception as ex:
    print("错误信息：%s" % ex)
