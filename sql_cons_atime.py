import sqlite3
conn = sqlite3.connect('users.sqlite')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS ADM(
TG_ID INTEGER ,
MAINDATA STRING,
MAINTIME STRING,
RU STRING,
UZ STRING
)
""")
first_insert_a = """
INSERT INTO ADM VALUES ("{}","{}"," "," "," " )
"""

upd_UZ = """
UPDATE ADM 
SET UZ = "{}" 
WHERE TG_ID = "{}"
"""
select_UZ= """
SELECT UZ
From ADM
WHERE TG_ID = "{}"
"""

upd_RU = """
UPDATE ADM 
SET RU = "{}" 
WHERE TG_ID = "{}"
"""
select_RU = """
SELECT RU
From ADM
WHERE TG_ID = "{}"
"""

upd_MAINDATA = """
UPDATE ADM 
SET MAINDATA = "{}" 
WHERE TG_ID = "{}"
"""
select_MAINDATA = """
SELECT MAINDATA
From ADM
WHERE TG_ID = "{}"
"""

upd_MAINTIME = """
UPDATE ADM 
SET MAINTIME = "{}" 
WHERE TG_ID = "{}"
"""
select_MAINTIME = """
SELECT MAINTIME
From ADM
WHERE TG_ID = "{}"
"""

get_id_from_adm = """
SELECT TG_ID 
FROM ADM
Where TG_ID = "{}"
"""