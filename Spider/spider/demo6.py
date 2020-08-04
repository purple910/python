"""Todo:抓取肯德基餐厅地址10页"""

from urllib import request, parse
import json

if __name__ == '__main__':

    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
    }

    for p in range(1, 11):

        data = {
            "cname": "北京",
            "pid": "",
            "pageIndex": str(p),
            "pageSize": "10"
        }

        data = parse.urlencode(data)
        req = request.Request(url=url, headers=headers, data=bytes(data, encoding="utf-8"))
        response = request.urlopen(req)
        res = response.read().decode("utf-8")
        res = json.loads(res)
        items = []
        for i in res['Table1']:
            item = {}
            rownum = i['rownum']
            storeName = i['storeName']
            addressDetail = i['addressDetail']
            cityName = i['cityName']

            item['rownum'] = rownum
            item['storeName'] = storeName
            item['addressDetail'] = addressDetail
            item['cityName'] = cityName

            items.append(item)

        f = open("KFC/KFC%s.json" %p, "w", encoding="utf-8")
        json.dump(items, f, ensure_ascii=False, indent=4)
