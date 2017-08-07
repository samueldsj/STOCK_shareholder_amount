# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html




import pymysql

def dbHandle():
    conn = pymysql.connect(
        host='localhost',
        db = 'STOCK',
        user='root',
        passwd='111111',
        charset='utf8',
        use_unicode=True
    )
    return conn


class XqgdhsPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        
        #每次抓取前改名：STOCK.Xq_gdhs_20170714
        sql = 'insert into STOCK.Xq_gdhs_20170802(name_code,date,gdhs) values(%s,%s,%s)'
        lis = (item['code'],item['date'],item['amount'])

        try:
            cursor.execute(sql,lis)
            dbObject.commit()
        except Exception as e:
            print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',e)
            dbObject.rollback()
        else:
            print('bbbbbbbbbbbbbbbbbbbbbb')
            dbObject.close()

        return item