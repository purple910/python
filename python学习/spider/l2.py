"""豆瓣 本周口碑榜"""
from lxml import etree
import requests

url = 'https://movie.douban.com/'
ua = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0"

with requests.get(url, headers={'User-Agent': ua}) as response:
    content = response.text     # html的内容

    html = etree.HTML(content)  # 分析html,返回DOM节点
    # titles = html.xpath("//div[@class='billboard-bd']//tr/td/a/text()")  # 返回文本列表
    # titles = html.xpath("//div[@class='billboard-bd']//tr//text()")  # 返回文本列表
    titles = html.xpath("//div[@class='billboard-bd']//tr")  # 返回文本列表
    for t in titles:
        # print(t)

        # s = t.strip()
        # print(s) if len(s) > 0 else print(end='')

        txt = t.xpath('.//text()')
        # print(txt)
        print(' '.join(map(lambda x: x.strip(), txt)))



