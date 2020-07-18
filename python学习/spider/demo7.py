"""TO:抓取肯德基店铺位置信息"""
from urllib import request, parse
import json

if __name__ == '__main__':

    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
    }

    data = {
        "cname": "北京",
        "pid": "",
        "pageIndex": "2",
        "pageSize": "10"
    }

    data = parse.urlencode(data)
    req = request.Request(url=url, headers=headers, data=bytes(data, encoding="utf-8"))
    response = request.urlopen(req)
    res = response.read().decode()
    res = json.loads(res)
    items = []
    for i in res['Table1']:
        item = {}

        rownum = i['rownum']
        storeName = i['storeName']
        addressDetail = i['addressDetail']
        provinceName = i['provinceName']

        item['rownum'] = rownum
        item['storeName'] = storeName
        item['addressDetail'] = addressDetail
        item['provinceName'] = provinceName

        items.append(item)


    f = open("KFC/KFC.json", "w", encoding="utf-8")
    json.dump(items, f, ensure_ascii=False, indent=4)
