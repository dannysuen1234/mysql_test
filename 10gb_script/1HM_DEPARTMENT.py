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


i = 18


command = '''INSERT IGNORE INTO `HumanResources_Department` VALUES (18,'Engineerings18','Research and Development','2008-04-29 18:30:00')'''



while i<17+100000:
	i +=1
	
	command = command + ''',('''+ str(i) + ",'Engineering" + str(i) + '''\','Research and Development','2008-04-29 18:30:00')'''
	if (i-17)%1000 == 0:
		i+=1
		mycursor.execute(command)
		mydb.commit()
		command =  '''INSERT IGNORE INTO `HumanResources_Department` VALUES (''' + str(i) + ",'Engineering" + str(i) + '''\','Research and Development','2008-04-29 18:30:00')'''

mycursor.execute(command)
mydb.commit()

curr_time = time.time()
print("time used = ", curr_time - prev_time , "s")

