# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CoronacrawlerSpider(CrawlSpider):
    name = 'coronacrawler'

    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]

        CoronacrawlerSpider.rules = [
            Rule(LinkExtractor(unique=True), callback='parse_item'),
        ]
        super(CoronacrawlerSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        item = {}
        item['url'] = response.url
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
