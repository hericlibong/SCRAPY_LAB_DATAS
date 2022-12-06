import scrapy


class FifalivescrapSpider(scrapy.Spider):
    name = 'fifalivescrap'
    allowed_domains = ['football-ranking.com']
    start_urls = ['http://football-ranking.com/fifa_rankings']

    def parse(self, response):
        table = response.xpath('//table[@class="ml-1 table table-striped table-bordered table-hover"]/tbody/tr')
        for item in table:
            rank = item.xpath('normalize-space(./td[1]/text())').get()
            moving = item.xpath('normalize-space(./td[1]/a/span/text())').get().strip('\xa0\xa0')
            country = item.xpath('normalize-space(./td[2]/span/text())').get()
            actual_points = item.xpath('normalize-space(./td[3]/b/text())').get()
            moving_points = item.xpath('normalize-space(./td[3]/a/span/text())').get()
            former_points = item.xpath('normalize-space(./td[4]/text())').get()
            former_rank = item.xpath('normalize-space(./td[5]/text())').get()
            yield {
                'rank':rank, 
                'moving':moving,
                'country':country,
                'actual points': actual_points,
                'moving points': moving_points,
                'former points':  former_points,
                'former rank': former_rank
            }
            
            
            
        
