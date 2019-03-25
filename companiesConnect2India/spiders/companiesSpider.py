import scrapy

class companiesSpider(scrapy.Spider):
	name = "connect2IndiaCompaniesBot"

	start_urls = ["https://connect2india.com/indian-company-directory"]

	def parse(self, response):
		companiesDict = {'CIN':[], 'Name':[]}
		companiesDict['CIN'].extend(response.xpath('//tr[@ngrepeat]/td[1]/div/text()').extract())		
		companiesDict['Name'].extend(response.xpath('//tr[@ngrepeat]/td[2]/div/a/text()').extract())	
		yield companiesDict

		nextPage = response.selector.xpath('//div[@class="col-xs-12 col-sm-6 pagination right"]/a/@href').extract_first()

		if nextPage is not None:
			yield response.follow(nextPage, callback=self.parse)
