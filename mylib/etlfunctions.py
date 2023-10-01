import sqlite3

def connect(name):
    # connect to a SQLite data base
    connect = sqlite3.connect(name)
    cursor = connect.cursor()
    return connect,cursor

def create(cursor):
    # create a table
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS payroll(
                    id INTEGER PRIMARY KEY,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    payamt FLOAT,
                    jobtitle TEXT
                ) 
                   ''')
def read(cursor):
    # read all data from table
    cursor.execute('SELECT * FROM payroll')
    return cursor.fetchall()

def update(cursor,id,first_name,last_name,payamt,jobtitle):
    # update student info
    updatequery = '''
    UPDATE payroll 
    SET first_name= '{}',
    last_name = '{}',
    payamt = '{}' ,
    jobtitle = '{}' 
    WHERE id = '{}'
    '''.format(first_name,last_name,payamt,jobtitle,id)
    cursor.execute(updatequery)

def delete(cursor,id):
    # delete a data from table
    cursor.execute('DELETE FROM payroll WHERE id = ?',(id,))
    
def insert(cursor,id,first_name,last_name,payamt,jobtitle):
     cursor.execute('''INSERT INTO payroll VALUES (?,?,?,?,?)''',\
         (id,first_name,last_name,payamt,jobtitle))