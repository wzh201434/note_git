# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class MysqldataPipeline(object):
	def __init__(self):
		self.connect = pymysql.connect('localhost','root','wzh960823','test')
		self.cursor = self.connect.cursor()
	#插入单行数据
	'''sql = """INSERT INTO test (id,author,mingyan)
			VALUES (1,'marktuwen','hello,world')"""
			'''
	sql = """INSERT INTO test (id,author,mingyan) VALUES (%s,%s,%s)"""
	val = [
		(2,'mayun','taobao.com'),
		(3,'liyanhong','baidu.com'),
		(4,'renzhengfei','huawei.com')
		]
	cursor.executemany(sql,val)
	db.commit()
	db.close()

	    
