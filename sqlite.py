import sqlite3

### Connect to SQLlite
connection = sqlite3.connect("Student.db")

### Create a cursor Object to insert record,create table
cursor=connection.cursor()

### Create the table

table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (NAME VARCHAR(25), CLASS VARCHAR(25),SECTION VARCHAR(25), MARKS INT)"""

cursor.execute(table_info)

### Insert Some More Records
cursor.execute('''Insert OR IGNORE Into STUDENT values('Shubham Sharma','GENERATIVE AI','A','90')''')
cursor.execute('''Insert OR IGNORE Into STUDENT values('Rohan Soni','GENERATIVE AI','A','100')''')
cursor.execute('''Insert OR IGNORE Into STUDENT values('JOHN','GENERATIVE AI','A','38')''')
cursor.execute('''Insert OR IGNORE Into STUDENT values('MUKESH','GENERATIVE AI','A','78')''')
cursor.execute('''Insert OR IGNORE Into STUDENT values('JACOB','GENERATIVE AI','A','63')''')

### DISPLAY ALL THE RECORDS
print("The inserted records are:")
data = cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)

## Commit Your changes in the database
connection.commit()
connection.close()