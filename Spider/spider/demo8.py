"""TOO:爬取百度翻译"""
# 导包
from urllib import request, parse
import json


if __name__ == '__main__':

    # 网页--》右键--》检查--》Network--》XHR（局部刷新） 发起一次请求，查找url
    url = "https://fanyi.baidu.com/sug"
    headers = {
        "user - agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
    }
    name = input("请输入要翻译的内容:")
    data = {
        "kw": name
    }

    # 对要查找的内容编码
    datas = parse.urlencode(data)
    # 构建请求，有 data 参数，说明是post请求，注意要转换成bytes格式
    req = request.Request(url=url, headers=headers, data=bytes(datas, encoding="utf-8"))
    # 发起请求
    response = request.urlopen(req)
    # 变量接收数据，解码
    res = response.read().decode("utf-8")
    # 将接收的数据用json转换成字符
    result = json.loads(res)
    # 用字典的取值方法，取值
    print(result["data"])
    print(result["data"][0]['v'])
    print(result["data"][0]['v'].split(';')[1].strip(' '))