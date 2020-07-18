from urllib import parse


d = {
    'wd': '中国'
}

u = parse.urlencode(d)  # 编码
url = 'https://www.baidu.com/s?{}'.format(u)
print(url)

print('中国'.encode('utf-8'))

print(parse.unquote(u))     # 解码
print(parse.unquote(url))
