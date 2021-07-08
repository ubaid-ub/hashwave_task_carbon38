import scrapy



class ItemsSpider(scrapy.Spider):

    name = 'items'
   
    def start_requests(self):		
   		url = 'https://www.carbon38.com/shop-all-activewear/tops'
   		yield scrapy.Request(url)

    def parse(self, response):
        print('parse')
