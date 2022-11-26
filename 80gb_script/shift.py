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

command = "INSERT IGNORE INTO `adventureworks`.`shift` VALUES  (1,'Day','1900-01-01 07:00:00','1900-01-01 15:00:00','1998-06-01 00:00:00')"


count = 0
while i<20000000:
	
	i +=1
	count +=1
	command +=",(" + str(i) + ",'Day','1900-01-01 07:00:00','1900-01-01 15:00:00','1998-06-01 00:00:00')"
	if i%1000 == 0:
		i+=1
		mycursor.execute(command)
		mydb.commit()
		command =  "INSERT IGNORE INTO `adventureworks`.`shift` VALUES  (" + str(i) + ",'Day','1900-01-01 07:00:00','1900-01-01 15:00:00','1998-06-01 00:00:00')"

mycursor.execute(command)
mydb.commit()

curr_time = time.time()
print("time used = s", prev_time - curr_time)

database_size_command = '''SELECT table_schema "DB Name",         ROUND(SUM(data_length + index_length) / 1024 / 1024, 1) "DB Size in MB"  FROM information_schema.tables  GROUP BY table_schema'''

mycursor.execute(database_size_command)
for item in mycursor:
	if item[0] == database_name:
		curr_size = item[1]

print("added data with size GB: ", float((curr_size - prev_size)/1000))
