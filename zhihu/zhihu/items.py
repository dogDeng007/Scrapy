# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 作者首页
    home_page = scrapy.Field()

    # 作者名称
    name = scrapy.Field()

    # 作者座右铭
    motto = scrapy.Field()

    # 评论时间
    cmt_time = scrapy.Field()

    # 评论点赞数
    stars = scrapy.Field()

    # 评论内容
    comments = scrapy.Field()
