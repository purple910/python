import requests
from bs4 import BeautifulSoup
import re

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
# url = 'http://www.netbian.com/dongman/'
# 页数循环
for i in range(1, 139):
    if i == 1:
        url = 'http://www.netbian.com/dongman/index.htm'
    else:
        url = 'http://www.netbian.com/dongman/index_{}.htm'.format(i)
        # print(url)
        response = requests.get(url, headers={'User-Agent': ua})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        list = soup.find(name='div', attrs='list')
        for li in list.find_all('li'):
            # print(img.attrs['src'])
            for a in li.children:
                if a.name == 'a':
                    src = 'http://www.netbian.com' + a.attrs['href']
                    # 截取连接里的数字作为图片的名称(这里可以自己想怎么弄就怎么弄)
                    n = re.search(r'\d+', a.attrs['href'])[0]
                    # print(n)
                    # print(src)
                    res = requests.get(src, headers={'User-Agent': ua})
                    s = BeautifulSoup(res.text, 'html.parser')
                    p = s.find(name='p')
                    # print(p)
                    img = p.img.attrs['src']
                    # print(img)
                    # 判断地址是否为空
                    if not img:
                        continue
                    with requests.get(img, headers={'User-Agent': ua}) as resp:
                        # print(resp.status_code)
                        resp.raise_for_status()
                        resp.encoding = res.apparent_encoding
                        # 将图片内容写入
                        with open('E://paper//{}.jpg'.format(n), 'wb') as f:
                            f.write(resp.content)
                            f.close()
