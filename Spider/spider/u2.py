import urllib.request

# User-Agent是爬虫与反爬虫的第一步
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0
ua_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
# 通过urllib2.Request()方法构造一个请求对象
# request = urllib.request.Request('http://www.baidu.com/')
request = urllib.request.Request('http://www.baidu.com/', headers=ua_headers)
response = urllib.request.urlopen(request)
html = response.read()

print(html)
print(request.get_header('User-agent'))
