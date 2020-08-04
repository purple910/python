from urllib import parse


d = {
    'id': 1,
    'name': '张三',
    'url': 'http://www.magedu.com/python?id=1&name=tom'
}

u = parse.urlencode(d)
print(u)
