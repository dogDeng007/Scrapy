# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaojiejieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 上传时间
    upload_times = scrapy.Field()

    # 照片链接
    pictures = scrapy.Field()
