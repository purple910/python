from urllib.request import urlopen
from http.client import HTTPResponse

url = 'http://www.bing.com'

response = urlopen(url=url, timeout=5)
print(response.closed)

# while response:
print(type(response))
print(response.status, response.reason)
print(response.read())
print(response.geturl())
print(response.info())

print(response.closed)
