import pymongo
myconnect=pymongo.MongoClient("mongodb://localhost:27017")
mydb=myconnect["pythonDatabase"]
mycol=mydb["login"]
def signup():
    print("signup")
    username=input("Enter the name:")
    userId=input("Enter the userId:")
    password=input("Enter the password:")
    conformpassword=input("Enter the conform password:")
    if(password==conformpassword):
        return
    userdata={"Username":username,
              "_Userid":userid,
              "Password":password}
    for eachDocument in mycol.find():
        if(eachDocument["userid"]==userid):
           break
        else:
            mycol.insert_one(userdata)
            print("user registered successfully")
def signin():
    print("signin")
    userid=input("Enter userid:")
    password=input("Enter password:")
    for eachDocument in mycol.find():
        if(eachDocument["userid"]==userid):
            print("login successfully")
            break
    else:
        print("correct username or password")
def update_account():
    print("update account")
    Changeusername=input("Enter the new username:")
    Changepassword=input("Enter the new password:")
    conformpassword=input("Re-enter the password:")
    print("user registered successfully")
    
def exit():
    print("Thank you for using our program!")
    sys.exit()
while True:
    print("1. Signup")
    print("2. Signin")
    print("3. Update Account")
    print("4. Exit")   
    choice = input("Enter your choice: ")
    if choice == "1":
        signup()
    elif choice == "2":
        signin()
    elif choice == "3":
        update_account()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")







##import pymongo
##
##myclient=pymongo.MongoClient("mongodb+srv://sathuryalakshmi29:<lsathurya29>@cluster0.4m0qfos.mongodb.net/?retryWrites=true&w=majority")
##mydb=myclient["pythonDatabase"]
##mycol=mydb["login"]
##
##def signup():
##    print("signup")
##    username=input("Enter user name")
##    emailid=input("Enter email id")
##    password=input("Enter password")
##    conformPassword=input("Re-enter password")
##    if(password!=conformPassword):
##        return
##    userDetail={"username":username,"emailid":emailid,"password":password}
##    for eachDocument in mycol.find():
##        if(eachDocument["emailid"]==emailid):
##            break
##    else:
##        mycol.insert_one(userDetail)
##        print("user registered successfully")
##def signin():
##    print("signin")
##    emailid=input("Enter email id")
##    password=input("Enter password")
##    for eachDocument in mycol.find():
##        if(eachDocument["emailid"]==emailid):
##            print("login successfully")
##            break
##    else:
##        print("incorrect username or password")
##
##def update_account():
##    print("update account"
##    Change_username=input("Enter the new username:")
##    Change_password=input("Enter the new password:")
##    conform_password=input("Re-enter the password:")
##    print("user registered successfully")
##
##        
##
##while(True):
##    print("1->signup")
##    print("2->signin")
##    print("3->update account")
##    print("4->exit")
##    choice=int(input("Enter your choice"))
##    if(choice==1):
##        signup()
##    elif(choice==2):
##        signin()
##    elif(choice==3):
##        update_account()
##    elif(choice==4):
##        print("exit")
##        break
##    else:
##        print("invalid choice.please try again.")

##
##import pymongo
##myclient=pymongo.MongoClient("mongodb://localhost:27017")
##mydb=myclient["pythonDatabase"]
##mycol=mydb["login"]
##def signup():
##    print("signup")
##    username=input("Enter user name:")
##    emailid=input("Enter email id:")
##    password=input("Enter password:")
##    confirmPassword=input("Re-enter password:")
##    if(password!=confirmPassword):
##        return
##    userDetail={"username":username,"emailid":emailid,"password":password}
##    for eachDocument in mycol.find():
##        if(eachDocument["emailid"]==emailid):
##            break
##    else:
##        mycol.insert_one(userDetail)
##        print("user registered successfully")
##def signin():
##    print("signin")
##    emailid=input("Enter email id")
##    password=input("Enter password")
##    for eachDocument in mycol.find():
##        if(eachDocument["emailid"]==emailid):
##            print("login successfully")
##            break
##    else:
##        print("incorrect username or password")
##def update_account():
##    username = input("Enter your username: ")
##    password = input("Enter your password: ")
##    if username == "admin" and password == "password":
##        new_password = input("Enter a new password:")
##        print("Account updated successfully!")
##    else:
##        print("Invalid username or password. Please try again.")
##        update_account()
##def exit():
##    p
##def main():
##    while(True):
##        print("1->signup")
##        print("2->sign in")
##        print("3-> update account")
##        print("4->exit")
##        choice=int(input("Enter your choice"))
##        if(choice==1):
##            signup()
##        elif(choice==2):
##            signin()
##        elif(choice==3):
##            update_account()
##        elif(choice==4):
##            print("exit")
##            break
##        else:
##            print("invalid choice. Please try again.")
##
##        main()



##import pymongo
##myclient=pymongo.MongoClient("")
##mydb=myclient["pythonDatabase"]
##mycol=mydb["login"]
##def sign_up():
##    username = input("Enter your username: ")
##    emailid = input("Enter your email id: ")
##    password = input("Enter your password: ")
##    conformPassword = input("Re_enter your password: ")
##    if(password!=confirmPassword):
##        return
##    userDetail={"username":username,"emailid":emailid,"password":password}  
##    for eachDocument in mycol.find():
##        if(eachDocument["emailid"]==emailid):
##            break
##    else:
##        mycol.insert_one(userDetail)
##        print("user registered successfully")
##def sign_in():
##    username = input("Enter your username: ")
##    password = input("Enter your password: ")
##def update_account():
##    username = input("Enter your username: ")
##
##while True:
##    print("1. Sign Up")
##    print("2. Sign In")
##    print("3. Update Account")
##    print("4. Exit")
##    
##    choice = input("Enter your choice: ")
##    
##    if choice == "1":
##        sign_up()
##    elif choice == "2":
##        sign_in()
##    elif choice == "3":
##        update_account()
##    elif choice == "4":
##        break
##    else:
##        print("Invalid choice. Please try again.")
##
##

        

