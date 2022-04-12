from scrapy import cmdline

cmdline.execute('scrapy crawl spider_zhihu -s LOG_FILE=all.log'.split())