# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from icecream import ic
import openpyxl as op

class ZhihuPipeline:
    def process_item(self, item, spider):

        ic(item)

        return item

class ExcelPipeline:

    def __init__(self):
        self.wb = op.Workbook()
        self.ws = self.wb.active
        self.ws.append(['作者首页', '作者名称', '作者座右铭', '评论时间', '评论点赞数', '评论内容'])

    def process_item(self, item, spider):
        line = [item['home_page'], item['name'], item['motto'], item['cmt_time'], item['stars'], item['comments']]
        self.ws.append(line)
        self.wb.save('../知乎.xlsx')
        print('知乎数据成功保存！')
        return item