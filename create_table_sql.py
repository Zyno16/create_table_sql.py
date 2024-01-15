import mysql.connector
try:
    conn = mysql.connector.connect(
        host     = "localhost",
        user     = "userpython",
        password = "123456",
        database = "arabicinfo"
        )
    cur =conn.cursor()
    cur.execute("CREATE TABLE emp (empno int primary key,empname varchar (99))")
                                

except mysql.connector.Error as e:
    print(e)
            
    
