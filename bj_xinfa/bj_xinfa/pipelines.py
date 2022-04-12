# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from icecream import ic
from bj_xinfa.settings import *
import pymongo
import openpyxl as op

class BjXinfaPipeline:

    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        collection = mongo_db_collection
        client = pymongo.MongoClient(host=host, port = port)
        db = client[dbname]
        self.post = db[collection]

    def process_item(self, item, spider):

        # 保存文件到本地
        with open('./北京菜价1.json', 'a+', encoding='utf-8') as f:
            lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(lines)

        ic(item)

        data = dict(item)
        self.post.insert(data)

        return item

class ExcelPipeline:

    def __init__(self):
        self.wb = op.Workbook()
        self.ws = self.wb.active
        self.ws.append(['蔬菜名称', '最低价格', '最高价格', '平均价格', '蔬菜产地', '菜价发布日期'])


    def process_item(self, item, spider):
        line = [item['prodName'], item['lowPrice'], item['highPrice'], item['avgPrice'], item['origin'],
                item['rlsDate']]
        self.ws.append(line)
        self.wb.save('./蔬菜.xlsx')
        print('蔬菜数据成功保存！')