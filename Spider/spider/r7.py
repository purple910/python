from urllib.parse import urlencode
import requests

urls = ['https://www.baidu.com/baidu?wd=python', 'https://www.baidu.com/baidu?wd=python']
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'

session = requests.Session()
with session:
    for url in urls:
        response = session.get(url=url, headers={'User-agent': ua})

        with response:
            print(type(response))
            print(response.url)
            print(response.status_code)
            print(response.cookies)
            print(response.request.headers)



