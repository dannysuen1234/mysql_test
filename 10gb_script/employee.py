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

command = "INSERT IGNORE INTO `adventureworks`.`employee` VALUES  (600,'481044938291',1012,'adventure-works\\syed0',273,'Pacific Sales Manager','1965-02-11 00:00:00','M','M','2003-04-15 00:00:00',0x01,20,30,0x01,0xDB92F2863CB79D429912800994D809FB,'2004-07-31 00:00:00')"


count = 0
while i<50000000:
	
	i +=1
	count +=1
	command +=",(" + str(i) + ",'481044938291',1012,'adventure-works\\syed0',273,'Pacific Sales Manager','1965-02-11 00:00:00','M','M','2003-04-15 00:00:00',0x01,20,30,0x01,0xDB92F2863CB79D429912800994D809FB,'2004-07-31 00:00:00')"
	if i%1000 == 0:
		i+=1
		mycursor.execute(command)
		mydb.commit()
		command =  "INSERT IGNORE INTO `adventureworks`.`employee` VALUES  (" + str(i) + ",'481044938291',1012,'adventure-works\\syed0',273,'Pacific Sales Manager','1965-02-11 00:00:00','M','M','2003-04-15 00:00:00',0x01,20,30,0x01,0xDB92F2863CB79D429912800994D809FB,'2004-07-31 00:00:00')"

mycursor.execute(command)
mydb.commit()

curr_time = time.time()
print("time used = s", curr_time - prev_time)

database_size_command = '''SELECT table_schema "DB Name",         ROUND(SUM(data_length + index_length) / 1024 / 1024, 1) "DB Size in MB"  FROM information_schema.tables  GROUP BY table_schema'''

mycursor.execute(database_size_command)
for item in mycursor:
	if item[0] == database_name:
		curr_size = item[1]

print("added data with size GB: ", float((curr_size - prev_size)/1000))
