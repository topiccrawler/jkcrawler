# -*- coding: utf-8 -*-
import scrapy
import json
import re


class InstagramSpider(scrapy.Spider):
    name = 'instagram'
    allowed_domains = ['instagram.com']
    start_urls = ['http://instagram.com/explore/tags/jk制服/?__a=1']

    def parse(self, response):
        graphql = json.loads(response.text)['graphql']
        for edge in graphql['hashtag']['edge_hashtag_to_media']['edges']:
            yield response.follow('/p/' + edge['node']['shortcode'] + '/', callback=self.parse_post)
        if graphql['hashtag']['edge_hashtag_to_media']['page_info']['has_next_page']:
            yield response.follow(
                '?__a=1&max_id=' + graphql['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor'])

    def parse_post(self, response):
        data = json.loads(re.findall(
            r'=\s*(.+);', response.css('body script::text').get()
        )[0])
        yield {'image_urls': [edge['node']['display_url'] for post_page in data['entry_data']['PostPage'] for edge in
                              post_page['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']]}
