# -*- coding: utf-8 -*-
import scrapy


class RyoryoChanTumblrSpider(scrapy.Spider):
    name = 'ryoryo-chan.tumblr'
    allowed_domains = ['ryoryo-chan.tumblr.com']
    start_urls = ['https://ryoryo-chan.tumblr.com/page/{}'.format(i) for i in range(20)]

    def parse(self, response):
        yield {'image_urls': response.css('#posts div.main figure > img::attr("src")').getall()}
