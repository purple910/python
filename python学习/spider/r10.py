# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=02003390_7_hao_pg&wd=aaaa&oq=%25E4%25BA%259A%25E9%25A9%25AC%25E9%2580%258A&rsv_pq=c600f6290025d8f8&rsv_t=2163JQdvXiGkGfAhVUYeAM0g0oPGt0aimPfe92Xd8txLneR8SPggb7w%2FGKjpQ1W%2FK3zRoBq6R9M&rqlang=cn&rsv_enter=1&rsv_dl=tb&inputT=2103&rsv_sug3=63&rsv_sug1=47&rsv_sug7=100&rsv_sug2=0&rsv_sug4=3251
import requests


try:
    url = "https://www.baidu.com/s"
    kv = {'wd': 'python'}
    r = requests.get(url=url, params=kv)
    print(r.request.url)
    print(r.status_code)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(len(r.text))
except Exception as e:
    print(e)
