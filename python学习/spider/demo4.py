import requests
import re
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print(r.status_code)
        return r.text
    except Exception as ex:
        print(ex)
        return ""


def parsePage(lt, html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        tlt = []
        plt = []

        for link in soup.find_all(name='p', attrs='productPrice'):
            plt.append(link.b.next_sibling)
        for link in soup.find_all(name='p', attrs='productTitle'):
            if len(link.span.next_sibling) > 0:
                tlt.append(link.span.next_sibling)
            else:
                tlt.append(link.span.previous_sibling)

        # print(len(plt))
        # print(len(tlt))
        # print(plt[0])
        # print(tlt[0])
        for i in range(len(tlt)):
            lt.append([plt[i], tlt[i]])
        # print(lt)
    except Exception as e:
        print(e)


def printGoodsList(lt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "名称"))
    count = 0
    for j in lt:
        count = count + 1
        print(tplt.format(count, j[0], j[1]))


def main():
    goods = '书包'
    depth = 2
    # https://list.tmall.com/search_product.htm?q=%CA%E9%B0%FC&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&xl=shubao_1&from=mallfp..pc_1_suggest
    start_url = "https://list.tmall.com/search_product.htm?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url     # + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except Exception as ex:
            print(ex)
    printGoodsList(infoList)


main()
