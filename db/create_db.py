# coding: UTF-8

import sqlite3

conn = sqlite3.connect('db.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE post
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    content VARCHAR(1000) NOT NULL,
    emitDate DATETIME NULL,
    expireDate DATETIME NULL
);
""")

conn.commit()

# cursor.execute("""
# INSERT INTO post (title, content, emitDate, expireDate)
# VALUES  ('Testing flask web service', '1st post at sqlite3 using flask framework.', '2018-01-10', '2018-01-20');
# """)

# conn.commit()

# cursor.execute("""
# INSERT INTO post (title, content, emitDate, expireDate)
# VALUES  ('New test', 'Adding another post into sqlite3.', '2018-07-04', NULL);
# """)

# conn.commit()

cursor.execute("""
CREATE TABLE test
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    description VARCHAR(20) NOT NULL
);
""")

conn.commit()

cursor.execute("""
INSERT INTO test (description)
VALUES  ('1st TEST');
""")

conn.commit()

print('OK.')

conn.close()
