# -*- coding: utf-8 -*-
import pymysql
form mysqldata.items import MysqldataItem
class mysqldata(scrapy.Spider):
	name = 'mysqldata'
	start_urls = ['http://lab.scrapyd.cn/']
	def parse(self,response):
		content = response.css('div.quote')
		item = MysqldataItem()
		for i in content:
			item['mingyan'] = i.css('.text::text').extract_first()
			item['author'] = i.css('.author::text').extract_first()
			yield item


