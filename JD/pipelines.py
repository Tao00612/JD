# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class MysqlPipeline:

    def open_spider(self, spider):
        self.conn = pymysql.connect(host='localhost', user='root', passwd='123', db='spidernew', port=3306,
                                    charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        data_tuple = (
         item['big_cate'], item['big_cate_link'], item['small_cate'], item['small_cate_link'], item['book_name'], item['author'], item['price'],item['link'])
        # print(data_tuple)
        sql = '''
            insert into jd_book values (0,"%s","%s","%s","%s","%s","%s","%s", "%s")
        '''
        # print(data_tuple)
        try:
            self.cur.execute(sql, data_tuple)
            self.conn.commit()
            print('爬取成功')
        except Exception:
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
