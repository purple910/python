from urllib.parse import urlencode
import requests

url = 'https://movie.douban.com/j/search_subjects'
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
d = {
    'type': 'tv',
    'tag': '热门',
    'page_limit': '50',
    'page_start': '0'
}
url = '{}?{}'.format(url, urlencode(d))

response = requests.request(method='GET', url=url, headers={
    'User-agent': ua
})

with response:
    print(response.text)
    print(response.status_code)
    print(response.url)
    print(response.headers)
    print(response.request.headers)

