# -*- coding: utf-8 -*-
import scrapy


# E:\Github\python\python学习\scripy_demo>scrapy genspider demo python123.io

class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['python123.io']

    # start_urls = ['http://python123.io/ws/demo.html']
    def start_requests(self):
        urls = [
            'http://python123.io/ws/demo.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open(fname, 'wb') as f:
            f.write(response.body)
            f.close()
        self.log('Saved file %s ' % fname)
