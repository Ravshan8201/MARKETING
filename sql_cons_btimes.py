import sqlite3
conn = sqlite3.connect('users.sqlite')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Book(
TG_ID INTEGER ,
MOMENTDATA STRING,
BOOKDATA STRING


)
""")
first_insert_b = """
INSERT INTO Book VALUES ("{}","{}","{}" )
"""

upd_MOMENTDA = """
UPDATE Book 
SET MOMENTDA = "{}" 
WHERE TG_ID = "{}"
"""
select_MOMENTDA = """
SELECT MOMENTDA
From Book
WHERE TG_ID = "{}"
"""

upd_BOOKDATA = """
UPDATE Book 
SET BOOKDATA = "{}" 
WHERE TG_ID = "{}"
"""
select_BOOKDATA = """
SELECT BOOKDATA
From Book
WHERE TG_ID = "{}"
"""

get_id_from_b = """
SELECT TG_ID 
FROM Book
Where TG_ID = "{}"
"""