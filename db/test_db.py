# coding: UTF-8

import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

tables = ['post', 'test']

for table in tables:
    cursor.execute(f'SELECT * FROM {table}')

    rows = cursor.fetchall()

    print(rows)

    #for row in rows:
    #    print(row)