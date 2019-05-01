# -*- coding: utf-8 -*-
import scrapy


class MakooooonTumblrSpider(scrapy.Spider):
    name = 'makooooon.tumblr'
    allowed_domains = ['makooooon.tumblr.com']
    start_urls = ['https://makooooon.tumblr.com/page/{}'.format(i) for i in range(94)]

    def parse(self, response):
        yield {'image_urls': response.css('figure::attr("data-highres")').getall()}
