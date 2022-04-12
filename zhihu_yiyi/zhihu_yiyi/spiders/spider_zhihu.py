import scrapy
from zhihu_yiyi.items import ZhihuYiyiItem
import time
from icecream import ic

'''
https://www.zhihu.com/api/v4/questions/288017836/root_comments?limit=10&offset=0&order=normal&status=open
https://www.zhihu.com/api/v4/questions/288017836/root_comments?limit=10&offset=10&order=normal&status=open
https://www.zhihu.com/api/v4/questions/288017836/root_comments?limit=10&offset=20&order=normal&status=open
https://www.zhihu.com/api/v4/questions/288017836/root_comments?limit=10&offset=20&order=normal&status=open
https://www.zhihu.com/api/v4/questions/288017836/root_comments?limit=10&offset=40&order=normal&status=open
https://www.zhihu.com/api/v4/questions/288017836/root_comments?limit=10&offset=50&order=normal&status=open
https://www.zhihu.com/api/v4/questions/288017836/root_comments?limit=10&offset=60&order=normal&status=open

'''

class SpiderZhihuSpider(scrapy.Spider):
    name = 'spider_zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def start_requests(self):
        for page in range(1, 55 + 1):
            print(f'.............正在爬取第{page}页.............')
            url = f'https://www.zhihu.com/api/v4/questions/288017836/root_comments?limit=10&offset={(page-1)*10}&order=normal&status=open'
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # 实例化item对象
        item = ZhihuYiyiItem()
        #ic(response.json())

        zhihu = response.json()['data']
        #ic(zhihu)
        for zh in zhihu:
            # 作者名称
            item['name'] = zh['author']['member']['name']

            # 作者座右铭
            item['motto'] = zh['author']['member']['headline']

            # 评论时间
            cmt_time = zh['created_time']
            item['cmt_time'] = time.strftime('%Y-%m-%d %H:%M', time.localtime(cmt_time))

            # 评论点赞数
            item['stars'] = zh['vote_count']

            # 评论内容
            item['comments'] = zh['content']

            yield item

