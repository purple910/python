## 创建scrapy项目
scrapy startproject 项目名  
cd 项目名  
## 在工程中产生一个scrapy爬虫
scrapy genspider 文件名 要爬网址
## 配置产生scrapy爬虫
## 运行爬虫
scrapy crawl 文件名  
## 调试
scrapy crawl text -o text.json
scrapy crawl text -o text.jl
 scrapy shell url