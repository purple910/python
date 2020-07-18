# http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html

import requests
import re
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as ex:
        print(ex)
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        # 判断tr是否为标签
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string, tds[4].string])


def printUnivList(ulist, num):
    # {5} 指的是chr(12288)
    tplt = "{0:^10}\t{1:{5}^10}\t{2:^10}\t{3:{5}^10}\t{4:^10}"
    # print("{:^10}\t{:^6}\t{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "省市", "总分", "指标得分"))
    print(tplt.format("排名", "学校名称", "省市", "总分", "指标得分", chr(12288)))
    for i in range(num):
        st = ulist[i]
        print(tplt.format(st[0], st[1], st[2], st[3], st[4], chr(12288)))
    # print("Suc" + str(num))


def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)


main()
