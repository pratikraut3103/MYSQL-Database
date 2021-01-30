import mysql.connector


class Mysql_database:
    def __init__(self):
        '''
        The connection is initalized in the init method
        so the connnection will be done as the object of the class is initalize
        '''

        self.mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = 'pythondatabase',
        charset='utf8')
        print(self.mydb)

    def create_database(self):
        '''
        This function will create a scheme in the database
        '''
        mycursor = self.mydb.cursor()
        mycursor.execute("create database pythondatabase") # instead of mydatabase you can write any name that you want
        print('Database created')

    def show_databases(self):
        '''
        this function is used to show all the databases in your system
        '''
        mycursor = self.mydb.cursor()
        mycursor.execute('show databases')
        for _ in mycursor:
            print(_)

    def create_table(self):
        '''
        This function is used to create table
        '''
        mycursor = self.mydb.cursor()
        mycursor.execute("CREATE TABLE customers (name VARCHAR(20), address VARCHAR(255))")
        print('table created')

    def show_tables(self):
        '''
        This function is used to show tables
        '''
        mycursor = self.mydb.cursor()
        mycursor.execute("SHOW TABLES")

        for _ in mycursor:
          print(_)

    def alter_table(self):
        '''
        This function is used to alter table
        '''
        mycursor = self.mydb.cursor()
        mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
        print('table altered')

    def insert_into_table(self):
        '''
        this function is used to insert values in tables
        '''
        mycursor = self.mydb.cursor()
        sql_query = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        values = ("Pratik", "somewhere on earth")
        mycursor.execute(sql_query, values)
        self.mydb.commit()
        print(mycursor.rowcount, "record inserted.")

if __name__ =="__main__":
    md = Mysql_database()
    md.insert_into_table()
