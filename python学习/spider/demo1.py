# https://tvax2.sinaimg.cn/large/006yt1Omgy1gbdu6ml01gj315o0ppb1w.jpg
# https://tvax1.sinaimg.cn/large/006yt1Omgy1gbdtwie3fkj31e00xc1kx.jpg
import requests
import os

url = "https://tvax2.sinaimg.cn/large/006yt1Omgy1gbdu6ml01gj315o0ppb1w.jpg"
root = "E://paper//"
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)

    if not os.path.exists(path):
        r = requests.get(url=url)
        print(r.status_code)
        r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
        print("successful")
    else:
        print("已存在")
except Exception as e:
    print(e)
