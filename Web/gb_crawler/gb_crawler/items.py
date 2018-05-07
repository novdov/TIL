# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# scrapy.Item 클래스를 상속 받음
class GbCrawlerItem(scrapy.Item):
    title = scrapy.Field()
    s_price = scrapy.Field()
    o_price = scrapy.Field()
    discount_rate = scrapy.Field()
    pass
