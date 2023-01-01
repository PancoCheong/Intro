# ------------------------------------------ myproject\myproject\db_mysql.py ------------------------------------------
#- install mysql-connector-python package
#- created the myquotes database schema in MySQL
#-
# import sqlite3
import mysql.connector
from items import MyprojectItem                 # import the data model defined in items.py on parent folder

#-
# conn = sqlite3.connect('myquotes.db')         # if myquotes.db doesn't existed, it will create it
#-                                              # if myquotes.db existed, it will re-use it
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Abcd1234',
    database =  'myquotes'
)

#- implement cursor
curr = conn.cursor()
#-
#- create a db table (only if it is not existed)
curr.execute("""    drop table if exists quotes_table
            """)
curr.execute("""    create table if not exists quotes_table(
                        title text,
                        author text,
                        tags text
                    )
            """)
#- insert data
curr.execute("""    insert into quotes_table values (
                        'use Python to insert data',
                        'Panco Cheong',
                        'target db is sqlite'
                    )
            """)
#-
item = MyprojectItem()
item['title'] = ['Manually create item']
item['author'] = ['Panco']
item['tags'] = ['tag 1', 'tag 2', 'tag 3']
#-
# curr.execute("""    insert into quotes_table values (?, ?, ?)""", (
#-
curr.execute("""    insert into quotes_table values (%s, %s, %s)""", (
                                ', '.join(item['title']),
                                ', '.join(item['author']),
                                ', '.join(item['tags'])
                                )
                        )
conn.commit()
conn.close()
