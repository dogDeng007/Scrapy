import scrapy
from xiaojiejie.items import XiaojiejieItem

class SpiderXiaojiejieSpider(scrapy.Spider):
    name = 'spider_xiaojiejie'
    allowed_domains = ['kanxiaojiejie.com/']
    start_urls = ['http://kanxiaojiejie.com//']


    def start_requests(self):
        for page in range(1, 500+1):
            url = f'https://www.kanxiaojiejie.com/page/{page}'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = XiaojiejieItem()

        # 获取当前页面所有小姐姐信息
        divs = response.xpath('//*[@id="masonry"]/article')

        # 提取小姐姐照片和标题
        for div in divs:
            item['upload_times'] = div.xpath("./div[@class='masonry-inner']/h2[@class='entry-title']/a/text()").get()

            item['pictures'] = div.xpath("./div[@class='masonry-inner']/div[@class='entry-top']/a[@class='entry-thumbnail']/img[@class='attachment-gridzone-medium-h size-gridzone-medium-h wp-post-image']/@src").get()

            yield item  # 将获取到的数据抛给pipeline下载