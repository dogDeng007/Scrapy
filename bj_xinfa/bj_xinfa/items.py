# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BjXinfaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 蔬菜名称
    prodName = scrapy.Field()

    # 最低价
    lowPrice = scrapy.Field()

    # 最高价
    highPrice = scrapy.Field()

    # 平均价
    avgPrice = scrapy.Field()

    # 产地
    origin = scrapy.Field()

    # 发布日期
    rlsDate = scrapy.Field()