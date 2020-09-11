import scrapy


class SidehutleSpider(scrapy.Spider):
    name = 'sidehutle'
    start_urls = ['https://www.sidehustlenation.com/side-hustle-show/', ]

    def parse(self, response):
        titles = response.xpath('//tr/td[@class="column-3"]/a/text()')
        for i, title in enumerate(titles):
            yield {i:title.get()}
                
