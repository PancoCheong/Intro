# ------------------------------------------ myproject\myproject\db_sqlite.py ------------------------------------------
#-
import sqlite3
#-
conn = sqlite3.connect('myquotes.db')       # if myquotes.db doesn't existed, it will create it
#-                                          # if myquotes.db existed, it will re-use it
#- implement cursor
curr = conn.cursor()
#-
#- create a db table (only if it is not existed)
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

conn.commit()
conn.close()
