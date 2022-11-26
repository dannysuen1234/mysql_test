import mysql.connector
import time

hostname = "localhost"
username = "danny1234"
passward = "1234"
database_name = "adventureworks"

mydb = mysql.connector.connect(
  host= hostname, 
  user= username, 
  passwd = passward,
  database = "adventureworks"
)


mycursor = mydb.cursor()

prev_time = time.time()


i = i

database_size_command = '''SELECT table_schema "DB Name",         ROUND(SUM(data_length + index_length) / 1024 / 1024, 1) "DB Size in MB"  FROM information_schema.tables  GROUP BY table_schema'''

mycursor.execute(database_size_command)
for item in mycursor:
	if item[0] == database_name:
		prev_size = item[1]


command = '''INSERT IGNORE INTO `department` VALUES (18,'Engineerings18','Research and Development','2008-04-29 18:30:00')'''



while i<100000:
	i +=1
	
	command = command + ''',('''+ str(i) + ",'Engineering" + str(i) + '''\','Research and Development','2008-04-29 18:30:00')'''
	if (i-17)%1000 == 0:
		i+=1
		mycursor.execute(command)
		mydb.commit()
		command =  '''INSERT IGNORE INTO `department` VALUES (''' + str(i) + ",'Engineering" + str(i) + '''\','Research and Development','2008-04-29 18:30:00')'''

mycursor.execute(command)
mydb.commit()

curr_time = time.time()
print("time used = ", curr_time - prev_time , "s")


mycursor.execute(database_size_command)
for item in mycursor:
	if item[0] == database_name:
		curr_size = item[1]

print("added data with size GB: ", float((curr_size - prev_size)/1000))

