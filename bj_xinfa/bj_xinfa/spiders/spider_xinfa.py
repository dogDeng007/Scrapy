import scrapy
from bj_xinfa.items import BjXinfaItem
from icecream import ic

class SpiderXinfaSpider(scrapy.Spider):
    name = 'spider_xinfa'
    allowed_domains = ['www.xinfadi.com.cn']
    start_urls = ['https://www.xinfadi.com.cn']

    def start_requests(self):
        for page in range(1, 50+1):
            url = f'http://www.xinfadi.com.cn/getPriceData.html?limit=20&current={page}'
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        # 获取蔬菜列表
        veg_list = response.json()['list']

        for veg in veg_list:
            # 实例化scrapy对象
            item = BjXinfaItem()

            # 蔬菜名称
            item['prodName'] = veg['prodName']

            # 最低价格
            item['lowPrice'] = veg['lowPrice']

            # 最高价格
            item['highPrice'] = veg['highPrice']

            # 平均价格
            item['avgPrice'] = veg['avgPrice']

            # 产地
            item['origin'] = veg['place']

            # 日期
            rlsDate = veg['pubDate']
            item['rlsDate'] = ''.join(rlsDate).split(' ')[0]

            yield item


