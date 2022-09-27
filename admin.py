import mysql.connector
mycon = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='Schoolobj')
mycursor = mycon.cursor()
# mycursor.execute("CREATE TABLE Admin_Info (admin_id INT(4), Full_Name VARCHAR(20),Email VARCHAR(50), Password VARCHAR(20))")
# mycursor.execute("ALTER TABLE Admin_Info admin_id INT(4) PRIMARY KEY AUTO_INCREMENT")
class Admin:
        choice = input("Are You A New Admin or Old Admin:>")
        if choice == "New Admin":
            print("Maximum New Admin Reached")
            # def reg():
            #     Full_Name = input("What's your full name:>")
            #     Email = input("Enter your email:>")
            #     Password = input("Enter your password:>")
            #     myquery = "INSERT INTO Admin_info (Full_Name, Email, Password) VALUES(%s,%s,%s)"
            #     val = (Full_Name,Email,Password)
            #     mycursor.execute(myquery,val)
            #     mycon.commit()
            #     print(mycursor.rowcount, "has been successfully uploaded to database")
            # reg()  
        else:    
            def login():
                admin_email = input("What's your registered email:>")
                admin_password = input("What's your password:>")
                check = "SELECT * FROM Admin_Info WHERE Email=%s And Password =%s"
                val1 = (admin_email,admin_password)
                mycursor.execute(check,val1)
                if mycursor.fetchone():
                    print("Admin Login Successful")
                    ask = input("Admin Do you want to set question? Yes/No:>")
                    if ask == "Yes":
                        # for i in range(10):
                        question = input("Set Your Question;>")
                        answer = input("What's the answer?")
                        option1 = input("What's the first option:>")
                        option2 = input("What's the second option:>")
                        option3 = input("What's the third option:>")
                        ques = "INSERT INTO Question_Bank (QUESTION, ANSWER, Option1, Option2, Option3) VALUES(%s,%s,%s,%s,%s)"
                        ans = (question, answer,option1,option2,option3)
                        mycursor.execute(ques, ans)
                        mycon.commit()
                        print(mycursor.rowcount, "Question Upload Successfully")
                    else:
                        print("We will see you later then Admin")                
                else:
                    print("Incorrect details.... Retry or Create Admin")
                    
                
            login()        
            
        
            