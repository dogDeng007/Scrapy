# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import requests
import time
import random

class XiaojiejiePipeline:
    def process_item(self, item, spider):
        #print(item)

        # 创建文件夹
        if not os.path.exists('images'):
            os.mkdir('images')

        # 保存图片到本地
        with open('images/{}.jpg'.format(item['upload_times']), 'wb') as f:
            req = requests.get(item['pictures'])
            f.write(req.content)
            time.sleep(random.random() * 2) # 防止网站反爬加上延时处理

        return item

