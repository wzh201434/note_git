import scrapy

#创建类
class scrapydata(scrapy.Spider):
	#name赋值，必备
	name = 'scrapydata'
	#url
	start_urls = ['http://lab.scrapyd.cn/']
	def parse(self,response):
		content = response.css('div.quote')
		for i in content:
			body = i.css('.text::text').extract_first()
			with open('mingyan.txt','a+') as f:
				f.write(body)
				f.write('\n')
