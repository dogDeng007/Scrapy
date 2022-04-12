# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
import openpyxl as op

class ZhihuYiyiPipeline:
    def process_item(self, item, spider):
        return item


class ExcelPipeline:

    def __init__(self):
        self.wb = op.Workbook()
        self.ws = self.wb.active
        self.ws.append(['作者名称', '作者座右铭', '评论时间', '评论点赞数', '评论内容'])

    def process_item(self, item, spider):
        line = [ item['name'], item['motto'], item['cmt_time'], item['stars'], item['comments']]
        self.ws.append(line)
        self.wb.save('../知乎1.xlsx')
        print('数据保存中......')
        return item
