# -*- coding: utf-8 -*-
import scrapy
import json


class ApiVcBilibiliSpider(scrapy.Spider):
    name = 'api.vc.bilibili'
    allowed_domains = ['api.vc.bilibili.com']
    start_urls = [
        'https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=sifu&type=new&page_num={}&page_size=20'.format(i)
        for i in range(600)]

    def parse(self, response):
        for i in json.loads(response.text)['data']['items']:
            yield response.follow(
                'https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id=' + str(i['item']['doc_id']),
                meta={'image_urls': [picture['img_src'] for picture in i['item']['pictures']]},
                callback=self.parse_jk,
            )

    def parse_jk(self, response):
        item = json.loads(response.text)['data']['item']
        title = item['title']
        tags = [tag['tag'] for tag in item['tags']]
        description = item['description']
        if any('jk' in i for i in (title, *tags, description)):
            yield {
                'title': title,
                'tags': tags,
                'description': description,
                'image_urls': response.meta['image_urls'],
            }
