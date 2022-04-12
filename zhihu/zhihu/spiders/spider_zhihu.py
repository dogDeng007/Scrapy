import scrapy
from icecream import ic
from zhihu.items import ZhihuItem
import time
'''
https://www.zhihu.com/api/v4/answers/2140770635/root_comments?order=normal&limit=20&offset=40&status=open
https://www.zhihu.com/api/v4/answers/2140770635/root_comments?order=normal&limit=20&offset=60&status=open
https://www.zhihu.com/api/v4/answers/2140770635/root_comments?order=normal&limit=20&offset=80&status=open
'''

class SpiderZhihuSpider(scrapy.Spider):
    name = 'spider_zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']

    def start_requests(self):
        for page in range(1, 10 + 1):
            #url = f'https://www.zhihu.com/api/v4/answers/2140770635/root_comments?order=normal&limit=20&offset={(page-1)*20}&status=open'
            url =  f'https://www.zhihu.com/api/v4/answers/2142116963/root_comments?order=normal&limit=20&offset={(page)*20}&status=open'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # 实例化item对象
        item = ZhihuItem()
        #ic(response.json())

        zhihu = response.json()['data']
        #ic(zhihu)
        for zh in zhihu:
            # 作者首页
            item['home_page'] = 'https://www.zhihu.com/people/' + zh['author']['member']['url_token']

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

