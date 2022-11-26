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

i = 1

database_size_command = '''SELECT table_schema "DB Name",         ROUND(SUM(data_length + index_length) / 1024 / 1024, 1) "DB Size in MB"  FROM information_schema.tables  GROUP BY table_schema'''

mycursor.execute(database_size_command)
for item in mycursor:
	if item[0] == database_name:
		prev_size = item[1]

command = "INSERT IGNORE INTO `adventureworks`.`customer` VALUES  (29484,7,'AW00029483','I',0xFEE937821002B5419FCA78A1722CD660,'2004-10-13 11:15:07')"


count = 0
while i<50000000:
	
	i +=1
	count +=1
	command +=",(" + str(i) + ",7,'AW00029483','I',0xFEE937821002B5419FCA78A1722CD660,'2004-10-13 11:15:07')"
	if i%1000 == 0:
		i+=1
		mycursor.execute(command)
		mydb.commit()
		command =  "INSERT IGNORE INTO `adventureworks`.`customer` VALUES  (" + str(i) + ",7,'AW00029483','I',0xFEE937821002B5419FCA78A1722CD660,'2004-10-13 11:15:07')"

mycursor.execute(command)
mydb.commit()

curr_time = time.time()
print("time used = s", curr_time - prev_time)

mycursor.execute(database_size_command)
for item in mycursor:
	if item[0] == database_name:
		curr_size = item[1]

print("added data with size GB: ", float((curr_size - prev_size)/1000))
