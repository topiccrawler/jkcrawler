# -*- coding: utf-8 -*-
import scrapy


class SscatXyzTumblrSpider(scrapy.Spider):
    name = 'sscat-xyz.tumblr'
    allowed_domains = ['sscat-xyz.tumblr.com']
    start_urls = ['https://sscat-xyz.tumblr.com/search/jk/page/{}'.format(i) for i in range(3)]

    def parse(self, response):
        yield {'image_urls': response.css('#posts div.main figure.tmblr-full > img::attr("src")').getall()}
