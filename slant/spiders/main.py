# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MainSpider(CrawlSpider):
    name = 'main'
    allowed_domains = ['slant.co']
    start_urls = ['https://www.slant.co/options/110']


    r1 = Rule(LinkExtractor(allow=(r'www.slant.co/versus/\d*?/\d*?')), callback="parse_versus", follow=True)
    r2 = Rule(LinkExtractor(allow=(r'www.slant.co/options/\d*?')), callback="parse_option", follow=True)
    rules = (r1, r2)


    def parse_versus(self, response):
        pass

    def parse_option(self, response):
        d = {}

        xp = '//span[@class="Recommendations-Label agree"]/text()'
        try:
            d['agree'] = int(response.xpath(xp)[0].extract())
        except Exception as e:
            self.logger.exception(e)
        try:
            xp = '//span[@class="Recommendations-Label disagree"]/text()'
            d['disagree'] = int(response.xpath(xp)[0].extract())
        except Exception as e:
            self.logger.exception(e)

        try:
            d['questions'] = []
            for x in response.xpath('//*[@data-view="MasterOptionPageQuestionView"]'):
                d1 = {}
                d1['href'] = x.xpath('a/@href')[0].extract()
                d1['rank'] = x.xpath('a/span/text()')[0].extract()
                d1['text'] = x.xpath('a/div/text()')[0].extract()
                d['questions'].append(d1)
        except Exception as e:
            self.logger.exception(e)

        d['pros'] = []
        xp = '//div[@class="ComboAvatar-Target"]'
        for x in response.xpath(xp):
            d2 = {}
            try:
                d2['head'] = x.xpath('div/h3/text()')[0].extract().strip()
                d2['text'] = x.xpath('div/div/p/text()')[0].extract().strip()
                d['pros'].append(d2)
            except Exception as e:
                self.logger.exception(e)

        # pros
        d['tags'] = []
        xp = '//div[@data-view="SidebarTagView"]/a/@href'
        for x in response.xpath(xp).extract():
            d['tags'].append(x)

        d['commonly_compared'] = []
        xp = '//div[@data-view="CommonlyComparedOptionView"]/a/@href'
        for x in response.xpath(xp).extract():
            d['commonly_compared'].append(x)

        yield d
