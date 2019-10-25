# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class MWeiboSpider(scrapy.Spider):
    name = 'm.weibo'
    allowed_domains = ['m.weibo.cn']
    start_urls = ['https://m.weibo.cn/search?containerid=231522&q=%23%E5%A5%BD%E6%83%B3%E7%9C%8B%E4%BD%A0%E7%A9%BFjk%E7%9A%84%E6%A0%B7%E5%AD%90%23']

    def start_requests(self):
        for start_url in self.start_urls:
            yield SplashRequest(start_url, self.parse, args={'wait': 5})

    def parse(self, response):
        yield {'image_urls': list(
            map(lambda x: x.replace('orj360', 'large'), response.css('.weibo-media-wraps img::attr("src")').getall()))}
