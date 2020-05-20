import scrapy

class KrishaSpider(scrapy.Spider):
	name = "krisha"
	start_int = 57000000
	end_int = 58000000
	start_urls = [
        'https://krisha.kz/a/show/' + str(i) for i in range(start_int, end_int)]
	
	def parse(self, response):
		type = response.css('a span::text').getall()[2]
		title = response.css('div.offer__advert-title h1::text').get()
		city = response.css('div.offer__location span::text').get()
		if 'квартира' in title and city.split(',')[0] == 'Алматы' and type == 'Продажа квартир':
			yield {
				'title': title,
				'price': response.css('div.offer__price::text').get(),
				'city': city,
				'house':response.css('div.offer__advert-short-info::text').getall()[3],
				'floor':response.css('div.offer__advert-short-info::text').getall()[4],
				'area':response.css('div.offer__advert-short-info::text').getall()[5]
				}