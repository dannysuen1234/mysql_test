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

command = "INSERT IGNORE INTO `adventureworks`.`product` VALUES   (1,'Road-750 Black, 58','BK-R19B-58',0x01,0x01,'Black',100,75,343.6496,539.99,'58','CM ','LB ','20.79',4,'R ','L ','U ',2,31,'2003-07-01 00:00:00',NULL,NULL,0x1A1AB887B5A5D243A20D0230800490B9,'2004-03-11 10:01:36')"


count = 0
while i<400000000:
	
	i +=1
	count +=1
	command +=",(" + str(i) + ",'Road-750 Black, 58','BK-R19B-58',0x01,0x01,'Black',100,75,343.6496,539.99,'58','CM ','LB ','20.79',4,'R ','L ','U ',2,31,'2003-07-01 00:00:00',NULL,NULL,0x1A1AB887B5A5D243A20D0230800490B9,'2004-03-11 10:01:36')"
	if i%1000 == 0:
		i+=1
		mycursor.execute(command)
		mydb.commit()
		command =  "INSERT IGNORE INTO `adventureworks`.`product` VALUES   (" + str(i) + ",'Road-750 Black, 58','BK-R19B-58',0x01,0x01,'Black',100,75,343.6496,539.99,'58','CM ','LB ','20.79',4,'R ','L ','U ',2,31,'2003-07-01 00:00:00',NULL,NULL,0x1A1AB887B5A5D243A20D0230800490B9,'2004-03-11 10:01:36')"

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
