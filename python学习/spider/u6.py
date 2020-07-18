from urllib import parse
from urllib.request import urlopen, Request


ua_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
d = {
    'wd': '中国'
}

u = parse.urlencode(d)  # 编码
url = 'https://www.baidu.com/s?{}'.format(u)
print(url)
print(parse.unquote(url))

req = Request(url=url, headers=ua_headers)
print(req.get_full_url())
res = urlopen(req)
print(res.status)
with res:
    with open('baidu.html', 'wb+') as f:
        f.write(res.read())
        f.flush()


