"""动漫图片"""
import requests
from bs4 import BeautifulSoup
import random
import time
import re


# start_url = 'http://www.netbian.com/dongman/'
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
# 设置随机的user-agent
# file = open('User-Agent.txt', 'r')
# lines = file.read().split(',\n')

start = 1
url = ''

# 页数循环
for i in range(107, 139):
    if i == 1:
        url = 'http://www.netbian.com/dongman/index.htm'
    else:
        url = 'http://www.netbian.com/dongman/index_{}.htm'.format(i)
    # print(url)

    # 获取本页的内容
    # response = requests.get(url, headers={'User-Agent': lines[random.randint(0, 37)]})
    response = requests.get(url, headers={'User-Agent': ua})
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # 获取图片的a标签的地址(若时获取img里的地址其大小为 800*450)
    list = soup.find(name='div', attrs='list')
    for li in list.find_all('li'):
        # print(img.attrs['src'])
        for a in li.children:
            if a.name == 'a':
                src = 'http://www.netbian.com' + a.attrs['href']
                n = re.search(r'\d+', a.attrs['href'])[0]
                # print(n)
                # print(src)

                # 到达真实图片地址
                # with requests.get(src, headers={'User-Agent': lines[random.randint(0, 37)]}) as res:
                res = requests.get(src, headers={'User-Agent': ua})
                s = BeautifulSoup(res.text, 'html.parser')
                p = s.find(name='p')
                # print(p)
                img = p.img.attrs['src']
                # print(img)
                if not img:
                    continue

                # 下载
                with requests.get(img, headers={'User-Agent': ua}) as resp:
                    # print(resp.status_code)
                    resp.raise_for_status()
                    resp.encoding = res.apparent_encoding
                    with open('E://paper//{}.jpg'.format(n), 'wb') as f:
                        f.write(resp.content)
                        f.close()

                    print(str(i) + "---" + str(start))
                    start += 1
                    time.sleep(random.random() * 3)     # 设置随机间隔时间
                    # if start > 5:
                    #     exit()

