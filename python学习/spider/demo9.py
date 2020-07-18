from urllib.parse import urlencode
from urllib.request import urlopen, Request
import simplejson

# https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0
# https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0
url = 'https://movie.douban.com/j/search_subjects'
ua = '	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
d = {
    'type': 'tv',
    'tag': '热门',
    'page_limit': '50',
    'page_start': '0'
}
dv = {
    'type': 'movie',
    'tag': '热门',
    'page_limit': '50',
    'page_start': '0'
}

req = Request('{}?{}'.format(url, urlencode(d)), headers={
    'User-Agent': ua
})
print(req.get_full_url())

with urlopen(req) as res:
    # print(simplejson.loads(res.read()))
    subject = simplejson.loads(res.read())
    print(type(subject))
    print(subject)

