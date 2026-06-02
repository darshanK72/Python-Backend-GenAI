import mysql.connector as connector
class DbHelper:
    def __init__(self):
        try:
            self.con = connector.connect(host="localhost",port="3306",user="root",password="darshan@123",database="company_db")
            print("Connection Created!!!")

        except Exception as e:
            print(e)

    def createTable(self,query):
        cur = self.con.cursor()
        cur.execute(query)
        print("Table Created Successfully!!!")

    def insert(self,query):
        cur = self.con.cursor()
        cur.execute(query)
        print("Inserted 1 Record Successfully!!!")

    def commit(self):
        self.con.commit()

    def getAll(self):
        cur = self.con.cursor()
        cur.execute("select * from student")
        for row in cur:
            print(row)




