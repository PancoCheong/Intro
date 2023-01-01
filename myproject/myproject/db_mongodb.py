# ------------------------------------------ myproject\myproject\db_mysql.py ------------------------------------------
# - install pymongo package
# -
import pymongo
# import the data model defined in items.py on parent folder
from items import MyprojectItem

# - see the parameter in MongoDB Compass (GUI)
conn = pymongo.MongoClient(
    'localhost',
    27017
)
# - create DB
db = conn['myquotes']
# - create table
collection = db['quotes_table']
# -
# -
item = MyprojectItem()
item['title'] = ['Manually create item']
item['author'] = ['Panco']
item['tags'] = ['tag 1', 'tag 2', 'tag 3']
# -
# - use dict() to store data into MongoDB
collection.insert_one(dict(item))

# conn.commit()
# conn.close()
