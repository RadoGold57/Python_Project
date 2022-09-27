# import os
import mysql.connector
mycon = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='Schoolobj')
mycursor = mycon.cursor()


# mycursor.execute("CREATE DATABASE Schoolobj")
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)
# mycursor.execute("CREATE TABLE Question_Bank (QUESTION VARCHAR(100), ANSWER VARCHAR(100), Option1 VARCHAR(50), Option2 VARCHAR(50), Option3 VARCHAR(50))")
print("Welcome To The SQI CbtTestExam")
choice= input("Are you Admin Or User?>")
if choice == "Admin":
    import admin
else:
    import users
            
        














