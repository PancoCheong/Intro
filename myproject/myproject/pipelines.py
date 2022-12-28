# ------------------------------------------ myproject\myproject\pipelines.py ------------------------------------------
#-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#-
# scraped data -> item containers -> json/csv files
#
# scraped data -> item containers -> pipeline -> SQL/Mongo database
#     uncomment ITEM_PIPELINES in settings.py
#     everytime my_quotes_spider.py yield the data, it sends to pipeline
#-   
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
#-
import sqlite3
#-
class MyprojectPipeline:                                  #panco: store the data into file, database etc
#-
#- constructor
    def __init__(self):
        self.create_connection()
        self.create_table()
#- 
    def create_connection(self):
        self.conn = sqlite3.connect('myquotes.db')
        self.curr = self.conn.cursor()
        print('myquotes.db database connection is opened')
#-
    def create_table(self):
        # self.curr.execute("""   drop table if exists quotes_table
        #                 """)
        self.curr.execute("""   create table if not exists quotes_table(
                                    title text,
                                    author text,
                                    tags text
                                )   
                        """)
#-
#-  ''.join(mylist) - concat a list into a single string, use ', ' as separator
    def store_db(self, item):
        self.curr.execute("""    insert into quotes_table values (?, ?, ?)""", (
                                ', '.join(item['title']),
                                ', '.join(item['author']),
                                ', '.join(item['tags'])
                                )
                        )
        self.conn.commit()
#-
    def close_connection(self):
        self.conn.close()
        print('myquotes.db database connection is closed')
#-    
#- each time when yield items is called, this method is executed
    def process_item(self, item, spider):
        self.store_db(item)
        print("Pipeline: " + item['title'][0])            #[0] print out the 1st element of the list
        print("    Type: " + str(type(item['title'])))    # print out the data type
        return item
#
#- destructor
    def __del__(self):
        self.close_connection()
#-