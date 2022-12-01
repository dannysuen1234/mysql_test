import mysql.connector
import time

hostname = "13.114.161.172"
username = "root"
passward = "root"
database_name = "adventureworks"
start_time = time.time()
while True:
    try:
        mydb = mysql.connector.connect(
        host= hostname, 
        user= username, 
        passwd = passward,
        database = database_name,
        port = 3306
        )
        break
    except:
        pass

mycursor = mydb.cursor()
command = '''SELECT * from address LIMIT 1'''
mycursor.execute(command)
complete_time = time.time()
print("Time used: %f s" % (complete_time - start_time))
