from urllib import parse
from urllib.request import urlopen, Request
import ssl


ua_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}

url = 'https://www.12306.cn/index/'
req = Request(url=url, headers=ua_headers)

# 忽略不信任的证书
context = ssl._create_unverified_context()
with urlopen(req, context=context) as res:
    print(res.read())



