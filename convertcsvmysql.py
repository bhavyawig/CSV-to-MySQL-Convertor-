import csv
import mysql.connector 

bhavya = mysql.connector.connect(host='localhost',
user='root',
passwd='Bhavya1!',
db='bhavya'
) # This command is used to make a connection with MySQL , it provides the hostname, username, password of MySQL and the name of database.

cursor=bhavya.cursor() # this connects the cursor to database.
file = open("studentdetails.csv", "r") # it reads the csv mile made which needs to the imported.
csv_data = csv.DictReader(file) # DictReader displays and presents the file in the form of Dictionary and reads the file into string csv_data.

for row in csv_data: 
       cursor.execute('insert into studentdetails1(name,course,score) values("{}", "{}", "{}")'.format(row["name"],row['course'],row["score"])) 
       #print(row)
# This loop traverses each row in the string csv_data and each line is transferred to the mysql table 'studentdetails1' with desried columns

bhavya.commit()
cursor.close()
print("done")
