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

command = "INSERT IGNORE INTO `adventureworks`.`salesorderheader` VALUES  (75124,1,'2004-07-31 00:00:00','2004-08-12 00:00:00','2004-08-07 00:00:00',5,0x01,'SO75120',NULL,'10-4030-018749',18749,18483,NULL,6,28374,28374,1,8925,'929849Vi46003',NULL,84.96,6.7968,2.124,93.8808,NULL,0xCF4F6AAE73FFD44CAF2C5993D00D4AFE,'2004-08-07 00:00:00')"


count = 0
while i<50000000:
	
	i +=1
	count +=1
	command +=",(" + str(i) + ",1,'2004-07-31 00:00:00','2004-08-12 00:00:00','2004-08-07 00:00:00',5,0x01,'SO75120',NULL,'10-4030-018749',18749,18483,NULL,6,28374,28374,1,8925,'929849Vi46003',NULL,84.96,6.7968,2.124,93.8808,NULL,0xCF4F6AAE73FFD44CAF2C5993D00D4AFE,'2004-08-07 00:00:00')"
	if i%1000 == 0:
		i+=1
		mycursor.execute(command)
		mydb.commit()
		command =  "INSERT IGNORE INTO `adventureworks`.`salesorderheader` VALUES  (" + str(i) + ",1,'2004-07-31 00:00:00','2004-08-12 00:00:00','2004-08-07 00:00:00',5,0x01,'SO75120',NULL,'10-4030-018749',18749,18483,NULL,6,28374,28374,1,8925,'929849Vi46003',NULL,84.96,6.7968,2.124,93.8808,NULL,0xCF4F6AAE73FFD44CAF2C5993D00D4AFE,'2004-08-07 00:00:00')"

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

