import pymysql

conn = pymysql.connect(host = "localhost",port=3307,user= "root",passwd="",database="collegedb")

cur = conn.cursor()

# Create Table
# createTable = """
#     CREATE TABLE student(
#         rollNo int(5),
#         firstName varchar(20),
#         lastName varchar(20),
#         marks int(5),
#         division char(1),
#         address varchar(50)
#     );
# """
# cur.execute(createTable)


# Insert Into 
# insertInto = """
#     INSERT INTO student(rollNo,firstName,lastName,marks,division,address)
#     VALUES(1,'Ravi','Sharma',89,'H','Nashik');
# """
# cur.execute(insertInto)
# cur.execute(insertInto)
# cur.execute(insertInto)

# Select * 
selectFrom = """
    SELECT * FROM student;
"""

cur.execute(selectFrom)

result = cur.fetchall()

print(result)

for ele in result:
    print(ele)

conn.commit()

conn.close()