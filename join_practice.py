import sqlite3
import os

os.remove("join.db")

con = sqlite3.connect("join.db")

cur = con.cursor()

cur.execute(
    """
    CREATE TABLE student(
        [name] VARCHAR(50) PRIMARY KEY,
        [program] VARCHAR(50)
    )
    """
)
cur.execute(
    """
    CREATE TABLE program(
        [name] VARCHAR(50) PRIMARY KEY,
        [degree] VARCHAR(50)
    )
    """
)

student_data = [
    ["Jack", "Biostatistics"],
    ["Costa", "CBB"],
    ["Hannah", "Biostatistics"],
]

cur.executemany("INSERT INTO student VALUES(?, ?)", student_data)

program_data = [["Biostatistics", "Masters"], ["CBB", "PhD"]]

cur.executemany("INSERT INTO program VALUES(?,?)", program_data)

students = cur.execute(
    """
    SELECT name from student
    WHERE program IN(
        SELECT name FROM program WHERE degree = 'PhD'
        )
    """
)

for line in students:
    print(line)

join = cur.execute(
    """
    SELECT s.name, p.degree
    FROM student s
    JOIN program p ON s.program = p.name
    """
)

for line in join:
    print(line)

con.commit()
con.close()
