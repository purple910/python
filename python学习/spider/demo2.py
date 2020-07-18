# http://m.ip138.com/ip.asp?ip=192.168.0.107

import requests

try:
    url = "http://m.ip138.com/ip.asp?ip="
    r = requests.get(url + '202.204.80.112')
    print(r.status_code)
    r.raise_for_status()
    print(r.text[-500:])
except Exception as e:
    print(e)
