import scrapy
import random

class QuotesSpider(scrapy.Spider):

	name = "items"
        	
	def start_requests(self):
		h = {	
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
		'cache-control': 'max-age=0',
		'cookie': 'webp=1; _pxvid=c03ce2c2-df34-11eb-be84-0242ac12000f; form_key=ak7A48LeflncRrHK; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; g38=grid; s38=undefined%3Aundefined; p38=120; PHPSESSID=72e47f53b59b243b8e8358cea20907b7; visitor_id=37424296; visitor_country_code=N%2FA; visits_counter_flag=1625670487; X-Magento-Vary=1a6e6799729a7e9386d54086f3dce42eda247d27; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; _gcl_au=1.1.1747288866.1625670493; _ga=GA1.2.429373273.1625670496; _gid=GA1.2.94238813.1625670496; RES_TRACKINGID=860420109323516; ResonanceSegment=1; _fbp=fb.1.1625670504278.2073532918; mage-cache-sessid=true; fs_uid=rs.fullstory.com#A2MHW#4672265347342336:5137896769265664#d0adcdfc#/1657206509; pxcts=dcb15df0-dfdd-11eb-8e7c-5dff03eb876d; __idcontext=eyJjb29raWVJRCI6Ikk2TEdYV1NSN0E3SDYzU1NIWEQ2MzZSSUNBNVJGUEo1UjZNNFRTUk9WSFlBPT09PSIsImRldmljZUlEIjoiSTZMR1hXU1I3SkNWR0JEQkg2NDc3TFFPRlJaU0RaSU9VN1U3TFgyVlI3VFE9PT09IiwiaXYiOiIzNFVKRUlBR1VRSVVCT09NNkNKTFk1VDRCWT09PT09PSIsInYiOjF9; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2MjU2NzAzMjksInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNhcmJvbjM4LmNvbS9zaG9wLWFsbC1hY3RpdmV3ZWFyL3RvcHMifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE2MjU3NDQ1NDUsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNhcmJvbjM4LmNvbS9zaG9wLWFsbC1hY3RpdmV3ZWFyL3RvcHMifSwiJHZpZXdlZF9pdGVtcyI6W3siVGl0bGUiOiJSSUJCRUQgVEFOSyIsIkl0ZW1JZCI6IjEwMzEwMyIsIlVybCI6Imh0dHBzOi8vd3d3LmNhcmJvbjM4LmNvbS9wcm9kdWN0L3JpYmJlZC10YW5rLXdoaXRlP2ludF9zb3VyY2U9Y2F0YWxvZ18rcHJvZHVjdF92aWV3JmludF9wb3NpdGlvbj0wJmludF92ZXJzaW9uPTAiLCJDYXRlZ29yaWVzIjpbIkNhcmJvbjM4IiwiU2hvcCBBbGwiLCJUb3BzICIsIlRhbmsgVG9wcyAiLCJXaW50ZXIgTGF5ZXJpbmciLCJUaGUgTGF5ZXIgRWRpdCIsIlVuZGVyICQxMDAiLCJXZXN0IENvYXN0IFN0eWxlIiwiUmliYmVkIERldGFpbHMiLCJSaWJiZWQiLCJHb2luZyBTb21ld2hlcmU/IiwiR3ltIEJhZyBCYXNpY3MiLCJVbmRlciAkMTAwIiwiUHJvZHVjdHMiLCJOZXcgWWVhciwgTmV3IFJvdXRpbmUiLCJXb3Jrb3V0IFdlZG5lc2RheSIsIlByZS1TcHJpbmciLCJGZWIgMjAyMCBTaXRld2lkZSIsIkZlYiBTaXRld2lkZSBTYWxlIiwiUmliYmVkIiwiVG9wcyIsIldvcmsoT3V0KSBGcm9tIEhvbWUiLCJVdGlsaXR5IEVkaXQiLCJCcmlnaHRzIiwiU2V0cyIsIkJlIENvb2wiLCJUcmF2ZWwgRWRpdCIsIkJhY2sgaW4gU3RvY2siLCJBbGwgRGF5IEVzc2VudGlhbHMiLCJVbmRlciAkMTAwIiwiQWxsIEdpZnRzIiwiTW9zdCBGYXZvcml0ZWQiLCIyMDIwdGhhbmtzMzAiLCJOb3Rld29ydGh5IiwiQmxhY2sgJiBXaGl0ZSBFZGl0ICIsIlNNU00yMDIxIiwiQmVzdCBTZWxsZXJzICIsIlNwcmluZyBGb3J3YXJkIiwiQ29yZSIsIlN1bW1lciBXaGl0ZXMiLCJFc3NlbnRpYWwgVG9wcyIsIlBhc3RlbHMgIiwiQW1lcmljYW5hICJdLCJNZXRhZGF0YSI6eyJQcmljZSI6Ijg4LjAwIn0sIkltYWdlVVJMIjoiaHR0cHM6Ly93d3cuY2FyYm9uMzguY29tL21lZGlhL2NhdGFsb2cvcHJvZHVjdC9jYWNoZS9hMjY3NDkwOWE4YmNlOTllZDYwZDA5YjUyNzRhY2YxYy9jL2EvY2FyYm9uMzgtcmliYmVkLXRhbmstdG9wcy13aGl0ZS0wMDYxLmpwZyIsIkxhc3RWaWV3ZWREYXRlIjoxNjI1NzQ0NTQ4LCJWaWV3cyI6Mn1dfQ==; pageViewed=7; private_content_version=519fc3b163427014c535d53dfb6d7e83; section_data_ids=%7B%22messages%22%3A1625744553%2C%22newsletter%22%3A1625744553%2C%22datalayer-user%22%3A1625676988%2C%22datalayer-basket%22%3A1625676988%7D; cjeventID=0; _uetsid=27bbe780df3511ebaf8ec15fdccc6bd6; _uetvid=27bc81a0df3511ebaf0eaf0c43bbbb6f',
		'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'none',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.',
    }
	
		url = 'https://www.carbon38.com/shop-all-activewear/tops'
		yield scrapy.Request(url,headers=h)
		
	
		
	def parse(self,response):
		pages=response.xpath('//select[@name="pager"]/option/@value').getall()
		
		for page in pages:
			user_agent_list=[
				'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
				'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
				'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
				'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
			]
			user_agent = random.choice(user_agent_list)
			h = {	
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
				'cache-control': 'max-age=0',
				'cookie': 'webp=1; _pxvid=c03ce2c2-df34-11eb-be84-0242ac12000f; form_key=ak7A48LeflncRrHK; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; g38=grid; s38=undefined%3Aundefined; p38=120; PHPSESSID=72e47f53b59b243b8e8358cea20907b7; visitor_id=37424296; visitor_country_code=N%2FA; visits_counter_flag=1625670487; X-Magento-Vary=1a6e6799729a7e9386d54086f3dce42eda247d27; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; _gcl_au=1.1.1747288866.1625670493; _ga=GA1.2.429373273.1625670496; _gid=GA1.2.94238813.1625670496; RES_TRACKINGID=860420109323516; ResonanceSegment=1; _fbp=fb.1.1625670504278.2073532918; mage-cache-sessid=true; fs_uid=rs.fullstory.com#A2MHW#4672265347342336:5137896769265664#d0adcdfc#/1657206509; pxcts=dcb15df0-dfdd-11eb-8e7c-5dff03eb876d; __idcontext=eyJjb29raWVJRCI6Ikk2TEdYV1NSN0E3SDYzU1NIWEQ2MzZSSUNBNVJGUEo1UjZNNFRTUk9WSFlBPT09PSIsImRldmljZUlEIjoiSTZMR1hXU1I3SkNWR0JEQkg2NDc3TFFPRlJaU0RaSU9VN1U3TFgyVlI3VFE9PT09IiwiaXYiOiIzNFVKRUlBR1VRSVVCT09NNkNKTFk1VDRCWT09PT09PSIsInYiOjF9; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2MjU2NzAzMjksInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNhcmJvbjM4LmNvbS9zaG9wLWFsbC1hY3RpdmV3ZWFyL3RvcHMifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE2MjU3NDQ1NDUsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNhcmJvbjM4LmNvbS9zaG9wLWFsbC1hY3RpdmV3ZWFyL3RvcHMifSwiJHZpZXdlZF9pdGVtcyI6W3siVGl0bGUiOiJSSUJCRUQgVEFOSyIsIkl0ZW1JZCI6IjEwMzEwMyIsIlVybCI6Imh0dHBzOi8vd3d3LmNhcmJvbjM4LmNvbS9wcm9kdWN0L3JpYmJlZC10YW5rLXdoaXRlP2ludF9zb3VyY2U9Y2F0YWxvZ18rcHJvZHVjdF92aWV3JmludF9wb3NpdGlvbj0wJmludF92ZXJzaW9uPTAiLCJDYXRlZ29yaWVzIjpbIkNhcmJvbjM4IiwiU2hvcCBBbGwiLCJUb3BzICIsIlRhbmsgVG9wcyAiLCJXaW50ZXIgTGF5ZXJpbmciLCJUaGUgTGF5ZXIgRWRpdCIsIlVuZGVyICQxMDAiLCJXZXN0IENvYXN0IFN0eWxlIiwiUmliYmVkIERldGFpbHMiLCJSaWJiZWQiLCJHb2luZyBTb21ld2hlcmU/IiwiR3ltIEJhZyBCYXNpY3MiLCJVbmRlciAkMTAwIiwiUHJvZHVjdHMiLCJOZXcgWWVhciwgTmV3IFJvdXRpbmUiLCJXb3Jrb3V0IFdlZG5lc2RheSIsIlByZS1TcHJpbmciLCJGZWIgMjAyMCBTaXRld2lkZSIsIkZlYiBTaXRld2lkZSBTYWxlIiwiUmliYmVkIiwiVG9wcyIsIldvcmsoT3V0KSBGcm9tIEhvbWUiLCJVdGlsaXR5IEVkaXQiLCJCcmlnaHRzIiwiU2V0cyIsIkJlIENvb2wiLCJUcmF2ZWwgRWRpdCIsIkJhY2sgaW4gU3RvY2siLCJBbGwgRGF5IEVzc2VudGlhbHMiLCJVbmRlciAkMTAwIiwiQWxsIEdpZnRzIiwiTW9zdCBGYXZvcml0ZWQiLCIyMDIwdGhhbmtzMzAiLCJOb3Rld29ydGh5IiwiQmxhY2sgJiBXaGl0ZSBFZGl0ICIsIlNNU00yMDIxIiwiQmVzdCBTZWxsZXJzICIsIlNwcmluZyBGb3J3YXJkIiwiQ29yZSIsIlN1bW1lciBXaGl0ZXMiLCJFc3NlbnRpYWwgVG9wcyIsIlBhc3RlbHMgIiwiQW1lcmljYW5hICJdLCJNZXRhZGF0YSI6eyJQcmljZSI6Ijg4LjAwIn0sIkltYWdlVVJMIjoiaHR0cHM6Ly93d3cuY2FyYm9uMzguY29tL21lZGlhL2NhdGFsb2cvcHJvZHVjdC9jYWNoZS9hMjY3NDkwOWE4YmNlOTllZDYwZDA5YjUyNzRhY2YxYy9jL2EvY2FyYm9uMzgtcmliYmVkLXRhbmstdG9wcy13aGl0ZS0wMDYxLmpwZyIsIkxhc3RWaWV3ZWREYXRlIjoxNjI1NzQ0NTQ4LCJWaWV3cyI6Mn1dfQ==; pageViewed=7; private_content_version=519fc3b163427014c535d53dfb6d7e83; section_data_ids=%7B%22messages%22%3A1625744553%2C%22newsletter%22%3A1625744553%2C%22datalayer-user%22%3A1625676988%2C%22datalayer-basket%22%3A1625676988%7D; cjeventID=0; _uetsid=27bbe780df3511ebaf8ec15fdccc6bd6; _uetvid=27bc81a0df3511ebaf0eaf0c43bbbb6f',
				'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
				'sec-ch-ua-mobile': '?0',
				'sec-fetch-dest': 'document',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-site': 'none',
				'sec-fetch-user': '?1',
				'upgrade-insecure-requests': '1',
				'user-agent': user_agent,
    		}
			yield scrapy.Request(response.urljoin(page),headers=h,callback=self.parse_products)
		
		
	def parse_products(self, response):
		
		links=response.xpath('//div[@class="wrapper_image"]/a/@href').getall()
		for link in links:
			
			user_agent_list = [
				'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
				'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
				'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
				'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
				'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
				'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0',
				'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0',
				'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/79.0.3945.88 Safari/537.36',
				'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
				'Mozilla/5.0 (X11; Datanyze; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
				'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
				'Mozilla/5.0 (X11; Fedora;Linux x86; rv:60.0) Gecko/20100101 Firefox/60.0',
				'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',
				'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30',
				'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.3 Safari/534.24',
			]
			user_agent = random.choice(user_agent_list)
			
			h = {	
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
				'cache-control': 'max-age=0',
				'cookie': 'webp=1; _pxvid=c03ce2c2-df34-11eb-be84-0242ac12000f; form_key=ak7A48LeflncRrHK; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; g38=grid; s38=undefined%3Aundefined; p38=120; PHPSESSID=72e47f53b59b243b8e8358cea20907b7; visitor_id=37424296; visitor_country_code=N%2FA; visits_counter_flag=1625670487; X-Magento-Vary=1a6e6799729a7e9386d54086f3dce42eda247d27; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; _gcl_au=1.1.1747288866.1625670493; _ga=GA1.2.429373273.1625670496; _gid=GA1.2.94238813.1625670496; RES_TRACKINGID=860420109323516; ResonanceSegment=1; _fbp=fb.1.1625670504278.2073532918; mage-cache-sessid=true; fs_uid=rs.fullstory.com#A2MHW#4672265347342336:5137896769265664#d0adcdfc#/1657206509; pxcts=dcb15df0-dfdd-11eb-8e7c-5dff03eb876d; __idcontext=eyJjb29raWVJRCI6Ikk2TEdYV1NSN0E3SDYzU1NIWEQ2MzZSSUNBNVJGUEo1UjZNNFRTUk9WSFlBPT09PSIsImRldmljZUlEIjoiSTZMR1hXU1I3SkNWR0JEQkg2NDc3TFFPRlJaU0RaSU9VN1U3TFgyVlI3VFE9PT09IiwiaXYiOiIzNFVKRUlBR1VRSVVCT09NNkNKTFk1VDRCWT09PT09PSIsInYiOjF9; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2MjU2NzAzMjksInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNhcmJvbjM4LmNvbS9zaG9wLWFsbC1hY3RpdmV3ZWFyL3RvcHMifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE2MjU3NDQ1NDUsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNhcmJvbjM4LmNvbS9zaG9wLWFsbC1hY3RpdmV3ZWFyL3RvcHMifSwiJHZpZXdlZF9pdGVtcyI6W3siVGl0bGUiOiJSSUJCRUQgVEFOSyIsIkl0ZW1JZCI6IjEwMzEwMyIsIlVybCI6Imh0dHBzOi8vd3d3LmNhcmJvbjM4LmNvbS9wcm9kdWN0L3JpYmJlZC10YW5rLXdoaXRlP2ludF9zb3VyY2U9Y2F0YWxvZ18rcHJvZHVjdF92aWV3JmludF9wb3NpdGlvbj0wJmludF92ZXJzaW9uPTAiLCJDYXRlZ29yaWVzIjpbIkNhcmJvbjM4IiwiU2hvcCBBbGwiLCJUb3BzICIsIlRhbmsgVG9wcyAiLCJXaW50ZXIgTGF5ZXJpbmciLCJUaGUgTGF5ZXIgRWRpdCIsIlVuZGVyICQxMDAiLCJXZXN0IENvYXN0IFN0eWxlIiwiUmliYmVkIERldGFpbHMiLCJSaWJiZWQiLCJHb2luZyBTb21ld2hlcmU/IiwiR3ltIEJhZyBCYXNpY3MiLCJVbmRlciAkMTAwIiwiUHJvZHVjdHMiLCJOZXcgWWVhciwgTmV3IFJvdXRpbmUiLCJXb3Jrb3V0IFdlZG5lc2RheSIsIlByZS1TcHJpbmciLCJGZWIgMjAyMCBTaXRld2lkZSIsIkZlYiBTaXRld2lkZSBTYWxlIiwiUmliYmVkIiwiVG9wcyIsIldvcmsoT3V0KSBGcm9tIEhvbWUiLCJVdGlsaXR5IEVkaXQiLCJCcmlnaHRzIiwiU2V0cyIsIkJlIENvb2wiLCJUcmF2ZWwgRWRpdCIsIkJhY2sgaW4gU3RvY2siLCJBbGwgRGF5IEVzc2VudGlhbHMiLCJVbmRlciAkMTAwIiwiQWxsIEdpZnRzIiwiTW9zdCBGYXZvcml0ZWQiLCIyMDIwdGhhbmtzMzAiLCJOb3Rld29ydGh5IiwiQmxhY2sgJiBXaGl0ZSBFZGl0ICIsIlNNU00yMDIxIiwiQmVzdCBTZWxsZXJzICIsIlNwcmluZyBGb3J3YXJkIiwiQ29yZSIsIlN1bW1lciBXaGl0ZXMiLCJFc3NlbnRpYWwgVG9wcyIsIlBhc3RlbHMgIiwiQW1lcmljYW5hICJdLCJNZXRhZGF0YSI6eyJQcmljZSI6Ijg4LjAwIn0sIkltYWdlVVJMIjoiaHR0cHM6Ly93d3cuY2FyYm9uMzguY29tL21lZGlhL2NhdGFsb2cvcHJvZHVjdC9jYWNoZS9hMjY3NDkwOWE4YmNlOTllZDYwZDA5YjUyNzRhY2YxYy9jL2EvY2FyYm9uMzgtcmliYmVkLXRhbmstdG9wcy13aGl0ZS0wMDYxLmpwZyIsIkxhc3RWaWV3ZWREYXRlIjoxNjI1NzQ0NTQ4LCJWaWV3cyI6Mn1dfQ==; pageViewed=7; private_content_version=519fc3b163427014c535d53dfb6d7e83; section_data_ids=%7B%22messages%22%3A1625744553%2C%22newsletter%22%3A1625744553%2C%22datalayer-user%22%3A1625676988%2C%22datalayer-basket%22%3A1625676988%7D; cjeventID=0; _uetsid=27bbe780df3511ebaf8ec15fdccc6bd6; _uetvid=27bc81a0df3511ebaf0eaf0c43bbbb6f',
				'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
				'sec-ch-ua-mobile': '?0',
				'sec-fetch-dest': 'document',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-site': 'none',
				'sec-fetch-user': '?1',
				'upgrade-insecure-requests': '1',
				'user-agent': user_agent,
    		}
			
			
			yield scrapy.Request(response.urljoin(link),headers=h,callback=self.parse_details)

	def parse_details(self, response):    	
		
		breads=response.xpath('//div[@class="breadcrumbs"]//a/text()').getall()
		breadcrumbs=[]
		for b in breads:
			breadcrumbs.append(b.strip())
		
		image_url=response.xpath('//a[@class="cloud-zoom"]//@data-src').get()
		brand=response.xpath('//div[@class="brand"]/a/span/text()').get()
		product_name=response.xpath('//div[@class="product_name"]/span/text()').get()
		
		p=response.xpath('//div[@class="price "]/text()').get()
		price=p.strip()
		
		r=response.xpath('//div[@class="pdp_info_reviewCount"]/text()')[1].get()
		reviews=r.strip()
		
		color=response.xpath('//div[@class="product_color_title"]/span[@class="current"]/text()').get()
		description=response.xpath('//div[@class="value"]/p/text()').get()
		
		s=response.xpath('//p[@class="pdp_tab_box_par"]/text()')[2].get()
		s1=s.split()
		sku=s1[1]
		product_id=s1[4]
        
		yield {
			'breadcrumbs':breadcrumbs,
			'image_url':image_url,
			'brand':brand,
			'product_name':product_name,
			'price':price,
			'reviews':reviews,
			'color':color,
			'description':description,
			'sku':sku,
			'product_id':sku,
		}
