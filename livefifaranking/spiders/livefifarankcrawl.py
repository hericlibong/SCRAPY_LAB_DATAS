import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import unicodedata


class LivefifarankcrawlSpider(CrawlSpider):
    name = 'livefifarankcrawl'
    allowed_domains = ['football-ranking.com']
    start_urls = ['http://football-ranking.com']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//ul/li[@class="c-sidebar-nav-item"][3]/a'), callback='parse_item', follow=True),
        
        Rule(LinkExtractor(restrict_xpaths='.//nav[@aria-label="Page navigation"][1]/ul/li[@class="page-item"][2]/a'),callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='.//nav[@aria-label="Page navigation"][1]/ul/li[@class="page-item"][3]/a'),callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='.//nav[@aria-label="Page navigation"][1]/ul/li[@class="page-item"][4]/a'),callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        table = response.xpath('//table[@class="ml-1 table table-striped table-bordered table-hover"]/tbody/tr')
        for item in table:
            rank = item.xpath('normalize-space(./td[1]/text())').get()
            moving = item.xpath('normalize-space(./td[1]/a/span/text())').get()
            country = item.xpath('normalize-space(./td[2]/span/text())').get().strip(' ')
            actual_points = item.xpath('.//td[3]/b/text()').get() 
            if actual_points is None: 
                actual_points = item.xpath('normalize-space(.//td[3]/text())').get()
            moving_points = item.xpath('./td[3]/a/span/text()').get()
            former_points = item.xpath('normalize-space(./td[@class="d-none d-sm-table-cell"]/text())').get()
            former_rank = item.xpath('normalize-space(./td[5]/text())').get()
            
            yield {
                'rank':unicodedata.normalize('NFKD', rank), 
                'moving':moving,
                'country':unicodedata.normalize('NFKD',country),
                'actual points':unicodedata.normalize('NFKD',actual_points),
                'moving points':moving_points,
                'former points':former_points,
                'former rank': former_rank
            }
            
            
