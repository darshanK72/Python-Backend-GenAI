from dbHelper import DbHelper

helper = DbHelper()

# query = """create table student(
#     roll_no int(5),
#     student_name varchar(20),
#     student_marks int(3),
#     student_address varchar(50)
#     );
#     """

# helper.createTable(query)

# helper.insert("insert into student(roll_no,student_name,student_marks,student_address) values(101,'Darshan',88,'Nashik');")

# helper.commit()

helper.getAll()