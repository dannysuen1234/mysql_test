import mysql.connector
import time

hostname = "localhost"
username = "danny"
passward = "1234"

mydb = mysql.connector.connect(
  host= hostname, 
  user= username, 
  passwd = passward,
  database = "adventureworks"
)


mycursor = mydb.cursor()

prev_time = time.time()
print("OK")

i = 294

mycursor.execute("LOCK TABLES `HumanResources_Employee` WRITE")

command = '''INSERT INTO `HumanResources_Employee` VALUES (294,'295847284294','adventure-works\\ken0294',NULL,NULL,'Chief Executive Officer','1969-01-29','S','M','2009-01-14',1,99,69,1,'F01251E5-96A3-448D-981E-0F99D789110D294','2014-06-29 18:30:00')'''
mycursor.execute(command)
mydb.commit()


while i<294+100000:
	i +=1
	
	command_append = command + ''',(''' + str(i) + ''',\'295847284''' + str(i) +  '''\','adventure-works\\ken0'''+str(i) + '''\',NULL,NULL,'Chief Executive Officer','1969-01-29','S','M','2009-01-14',1,99,69,1,'F01251E5-96A3-448D-981E-0F99D789110D''' + str(i) + "','2014-06-29 18:30:00')"
	if (i-20777)%1000 == 0:
		i+=1
		mycursor.execute(command)
		mydb.commit()
		command =  "INSERT IGNORE INTO `HumanResources_Employee` VALUES(" + str(i) + ''',\'295847284''' + str(i) +  '''\','adventure-works\\ken0'''+str(i) + '''\',NULL,NULL,'Chief Executive Officer','1969-01-29','S','M','2009-01-14',1,99,69,1,'F01251E5-96A3-448D-981E-0F99D789110D''' + str(i) + "','2014-06-29 18:30:00')"

mycursor.execute(command)
mydb.commit()

curr_time = time.time()
print("time used = ", prev_time - curr_time)

