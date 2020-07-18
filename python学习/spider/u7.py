"""post请求"""

from urllib import parse
from urllib.request import urlopen, Request
import simplejson

ua_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
data = parse.urlencode({'name': '张三,@=/&*', 'age': '18'})
url = 'http://www.httpbin.org/post'

req = Request(url=url, headers=ua_headers)

with urlopen(req, data=data.encode()) as res:
    text = res.read()
    d = simplejson.loads(text)
    print(d)
    print(type(d))

    # with open('baidu.html', 'wb+') as f:
    #     f.write(res.read())
    #     f.flush()
