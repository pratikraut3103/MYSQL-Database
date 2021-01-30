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

if __name__ =="__main__":
    md = Mysql_database()
    md.create_table()
