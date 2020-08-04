import requests

cookie = {
    "gpsd": "b3c059bef6faa0fd56282xxxxxx",
    "JSESSIONID": "aaaTto6SLmxxxxxxxx",
    "gpid": "22bb5d4a3f824de78ad3d7fe7a0844f6",
    "gdxidpyhxdE": "M%2FOPyR5HMhg2qRDg2JQh9Z2KqygiCEXUUqpe0aqcwnTa%5CmsjKCoHoRRdnjJQAiCUcaAdEDrfiaKCP9ux7Sm2p6d69R24JWVPnHx0eHXgdo36PAY%2BD1BaTE8VJVw%2FDyImCiDbTRpdYL%2BXWArApjKJ31hgGTas1sGXOIdfAz0odXPdPDTg%3A1548427514478",
    " _9755xjdesxxd_": "32",
    "YD00000980905869%3AWM_NI": "zcykmdAFAGI4wEjxR%2BvX5ORpNMHi27FQebIhsdcSKxDk7TDy2y4kt13hjn4jV7ekyTlc%2BmR7Bs4a6DoM1eHXzS%2FgXa68mylIFXNyQd7Pjr%2FP2RvJSYwNTqwWgKcBsoRFSk0%3D" ,
    "YD00000980905869%3AWM_NIKE": "9ca17ae2e6ffcda170e2e6eed7c16f9c95aeb1b33d86b88ba2c15f979a9bbbbb648a8fb6acd065a1bbbe8eeb2af0fea7c3b92ababdb78cf070839a8fa8cc40b59ba699d121b688fbb0d17c8e93888ab13d868fab83cc64b1bcadb4ca7xxxxx773f2a7fxx76296e9ab8cfc60b0bde58ed13d82xx86cb54ba8de188db6bf6e8a39aef438688829ad470f590a693ae5cf28ebaabd253b5929c92f65da595ada3f265929a9d8cb337e2a3",
    "YD00000980905869%3AWM_TID": "zJgV%2FKPggm9BFUxxplJBzLdoNer3x",
}
headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/71.0.3578.98 Safari/537.36"
}
response = requests.get("https://dig.chouti.com/user/link/saved/1", cookies=cookie, headers=headers)

print(response.text)
