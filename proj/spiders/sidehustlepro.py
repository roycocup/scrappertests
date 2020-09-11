import scrapy
import logging


class SidehustleproSpider(scrapy.Spider):
    name = 'sidehustlepro'
    start_urls = ['http://www.sidehustlepro.co/podcast-episodes/']
    counter = 1

    def parse(self, response):
        titles = response.xpath('//article/div/div/h3/a/text()')
        for title in titles:
            yield {self.counter:title.get()}
            self.counter += 1

        next_page = response.css('.next::attr(href)').get()
        if next_page is not None:
            self.log('next page ' + next_page, logging.CRITICAL)
            yield scrapy.Request(next_page, callback=self.parse)