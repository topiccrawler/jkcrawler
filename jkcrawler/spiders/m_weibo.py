# -*- coding: utf-8 -*-
import scrapy
import json
from bs4 import BeautifulSoup


class MWeiboSpider(scrapy.Spider):
    name = 'm.weibo'
    allowed_domains = ['m.weibo.cn']
    start_urls = [
        *('https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D1%26q%3D%23%E5%A5%BD%E6%83%B3%E7%9C%8B%E4'
          '%BD%A0%E7%A9%BFjk%E7%9A%84%E6%A0%B7%E5%AD%90%23&page=' + str(i) for i in range(110)),
        *('https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%23%E5%A5%BD%E6%83%B3%E7%9C%8B%E4'
          '%BD%A0%E7%A9%BF%E5%88%B6%E6%9C%8D%E7%9A%84%E6%A0%B7%E5%AD%90%23&page=' + str(i) for i in range(120)),
    ]

    def parse(self, response):
        result = json.loads(response.text)
        if result.get('ok'):
            for card in result['data']['cards']:
                yield {
                    'user': card['mblog']['user']['screen_name'],
                    'text': card['mblog']['longText']['longTextContent'] if card['mblog'].get(
                        'isLongText') else BeautifulSoup(card['mblog']['text'], 'lxml').get_text(),
                    'image_urls': [pic['large']['url'] for pic in card['mblog']['pics']],
                }
