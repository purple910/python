import urllib3
from urllib.parse import urlencode
from urllib3.response import HTTPResponse

url = 'https://movie.douban.com/j/search_subjects'
ua = '	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
d = {
    'type': 'tv',
    'tag': '热门',
    'page_limit': '50',
    'page_start': '0'
}
url = '{}?{}'.format(url, urlencode(d))


with urllib3.PoolManager() as http:
    response = http.urlopen(method='GET', url=url, headers={
        'User-Agent': ua
    })
    print(type(response))
    # response: HTTPResponse = HTTPResponse()     # 写出来是为了要response的属性
    print(response.status)
    print(response.data)
