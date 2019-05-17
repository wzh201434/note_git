import pymysql
#连接数据库
db = pymysql.connect('localhost','root','******','test')

#创建cursor对象
cursor = db.cursor()

#sql固定格式，"""INSERT INTO table_name (table字段) VALUES (%s,%s)"""
sql = """INSERT INTO mysql (name,website) VALUES (%s,%s)"""

#val固定格式，[]要插入的相关数据
val = [('baidu','www.baidu.com'),('google','www.google.com'),('sougou','www.sougou.com')]

#执行插入，单一数据使用cursor.execute()
#多数据使用cursor.executemany()
cursor.executemany(sql,val)

#提交确认
db.commit()

#关闭连接
db.close()