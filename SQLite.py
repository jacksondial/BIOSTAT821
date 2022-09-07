"""SQLite."""
import sqlite3
import os

os.remove("example.db")

con = sqlite3.connect("example.db")

cur = con.cursor()

# This is the query that we want to execute against the database

cur.execute(
    """
    CREATE TABLE patient(
        [patient_id] INTEGER PRIMARY KEY,
        [name] TEXT,
        [grade] INTEGER)
    """
)

data0 = [
    [0, "Josh", 57],
    [1, "Mark", 93],
    [2, "Sierra", 36],
]

# for row in data0:
#     cur.execute("INSERT INTO patient VALUES(?, ?, ?)", row)

cur.executemany("INSERT INTO patient VALUES(?, ?, ?)", data0)

cur.execute(
    """
    INSERT INTO patient
    VALUES (4, 'Steven', 72)
    """
)

con.commit()

data = cur.execute(
    """
    SELECT * FROM patient
    """
)

for row in data:
    print(row)

con.close()


# create table Class(
#     students varchar[255],
#     instructor varchar[255]
# );
