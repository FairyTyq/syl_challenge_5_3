# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from douban.items import MovieItem

class AwesomeMovieSpider(CrawlSpider):
    name = 'awesome-movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/3011091/']

    rules = (
            Rule(LinkExtractor(allow=r'https://movie.douban.com/subject/\d+/?from=subject-page'), 
            callback='parse_item', 
            follow=True),
    )

    def parse_item(self, response):
        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i
        item = MovieItem()
        item['url'] = response.url
        item['name'] = response.xpath('//div[@id="wrapper"]/div[@id="content"]/h1/span/text()').extract()
        item['summary'] = response.xpath('//div[@id="link-report"]/span[1]/text()').extract()
        item['score'] = response.xpath('//strong[@class="ll rating_num"]/text()').extract()

        yield item
