# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CoronacrawlerSpider(CrawlSpider):
    name = 'coronacrawler'
    allowed_domains = [
        'https://www.michigan.gov/coronavirus/0,9753,7-406-98163_98173---,00.html']
    start_urls = [
        'http://https://www.michigan.gov/coronavirus/0,9753,7-406-98163_98173---,00.html/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
