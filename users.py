import mysql.connector
mycon = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='Schoolobj')
mycursor = mycon.cursor()

# mycursor.execute("CREATE TABLE Student_Info (ctm_id INT(4), Ful_Name VARCHAR(20), Address VARCHAR(50), Phone VARCHAR(11), Password VARCHAR(20))")
# mycursor.execute("ALTER TABLE Student_Info CHANGE ctm_id ctm_id INT(4) PRIMARY KEY AUTO_INCREMENT")
# mycursor.execute("ALTER TABLE Student_Info ADD UNIQUE(Phone);")
# mycursor.execute("ALTER TABLE Student_Info CHANGE ctm_id student_id INT(4)")

def login():
    score = 0
    choice = (input("Are You A New User or Old User:>").upper().strip())
    if choice == "NEW USER":
        print("Not accepting new user. Thank You")
        # Full_Name = input("What's your full name:>")
        # Address = input("Enter your Address:>")
        # Phone = input("Enter your phone number:>")
        # Password = input("Enter your password:>")
        # myquery = "INSERT INTO Student_info (Ful_Name, Address, Phone, Password) VALUES(%s,%s,%s,%s)"
        # val = (Full_Name,Address,Phone,Password)
        # mycursor.execute(myquery,val)
        # mycon.commit()
        # print(mycursor.rowcount, "has been successfully uploaded to database")
    else:
        print("Login To Your Account")
        user_Address = input("What's your registered Address:>")
        user_password = input("What's your password:>")
        check = "SELECT * FROM Student_Info WHERE Address=%s AND Password =%s"
        val1 = (user_Address,user_password)
        mycursor.execute(check,val1)
        print("Welcome back to your computer based test")
        if mycursor.fetchone():
            print("You have question 1 to answer.")
        for i in range(1):
            Q_id = int(input("Choose Your Question Number:>"))    
            check1 = "SELECT * FROM Question_Bank WHERE Question_ID = %s"
            val2 = (Q_id,)
            mycursor.execute(check1,val2)
            qi = mycursor.fetchone()
            print(qi[1])
            print(qi[2])
            print(qi[3])
            print(qi[4])
            answer = (input(":>").upper())
            check2 = "SELECT * FROM Question_Bank Where Answer = %s"
            val = (answer, )
            mycursor.execute(check2,val)
            mycursor.fetchall()
            if qi[-1] == answer:
                score += 2
            else: 
                score = 0
        print(f"Your total score is {score}")

login()
           
# def ridwan():
#     score = 0
     
# ridwan()
            
            