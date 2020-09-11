import scrapy


class GumtreeSpider(scrapy.Spider):
    name = 'gumtree'
    allowed_domains = ['www.gumtree.com/freebies/london']
    start_urls = ['http://www.gumtree.com/freebies/london/']

    def parse(self, response):
        pass
