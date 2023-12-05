##import pymongo
##
##myclient=pymongo.MongoClient("mongodb+srv://sathuryalakshmi29:lsathurya@cluster0.4m0qfos.mongodb.net/?retryWrites=true&w=majority")
##mydb=myclient["pythonDatabase"]
##mycol=mydb["login"]
##
##
##def update(personid):
##    print("1->update email")
##    print("2-> update name")
##    print("3-> update password")
##    choice=int(input("Enter your choice:"))
##    if(choice==1):
##        newEmail=input("Enter new email id:")
##        mycol.update_one({"_id":personid},{"$set":{"emailid":newEmail}})
##def homePage(personid):
##    print("1->update")
##    print("2->delete")
##    print("3->exit")
##    choice=int(input("Enter your choice:"))
##    if(choice==1):
##        update(personid)
##    elif(choice==2):
##        mycol.delete_one({"_id":personid})
##    elif(choice==3):
##        return 
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
##        result=mycol.insert_one(userDetail)
##        print("user registered successfully")
##        personId=result.inserted_id
##        homePage(personId)
##def signin():
##    print("signin")
##    emailid=input("Enter email id:")
##    password=input("Enter password:")
##    for eachDocument in mycol.find():
##        if(eachDocument["emailid"]==emailid):
##            print("login successfully")
##            break
##    else:
##        print("incorrect username or password")
##
##while(True):
##    print("1->signup")
##    print("2->signin")
##    print("3->exit")
##    choice=int(input("Enter your choice:"))
##    if(choice==1):
##        signup()
##    elif(choice==2):
##        signin()
##    elif(choice==3):
##        print("exit")
##        break
##    else:
##        print("invalid choice")
##def exit():
##    print("Thank you")











##import pymongo
##
##myclient=pymongo.MongoClient("mongodb://localhost:27017")
##mydb=myclient["pythonDatabase"]
##mycol=mydb["login"]
##def delete():
##    mycol.delete_one({"_id":userid})
##def username():
##    new_username=input("Enter new username")
##    mycol.update_one({"_id":userid},{"$set":{"username":new_username}})
##def email():
##    new_emailid=input("Enter email id")
##    mycol.update_one({"_id":userid},{"$set":{"username":new_emailid}})
##def password():
##    new_password=input("Enter password")
##    con_password=input("Enter password again:")
##    if(new_password==con_password):
##        mycol.update_one({"_id":userid},{"$set":{"username":new_password}})
##    else:
##        print("Enter the password correctly:")
##        con_password=input("Enter the password again:")
##def update(userid):
##        print("1->change Username")
##        print("2->change Emailid")
##        print("3->change Password")
##        print("4->exit")
##        choice=int(input("Enter your choice:"))
##        if(choice==1):
##            username()
##        elif(choice==2):
##            email()
##        elif(choice==2):
##            password()
##        elif(choice==4):
##            return
##        else:
##            print("invalid choice")
##def homepage(userid):
##        print("1->update")
##        print("2->delete")
##        print("3->exit")
##        choice=int(input("Enter your choice:"))
##        if(choice==1):
##            update(userid)
##        elif(choice==2):
##            delete(userid)
##        elif(choice==3):
##            return
##        else:
##            print("invalid choice")
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
##        result=mycol.insert_one(userDetail)
##        print("user registered successfully")
##        homepage(result)
##def signin():
##    print("signin")
##    emailid=input("Enter email id:")
##    password=input("Enter password:")
##    for eachDocument in mycol.find():
##        if(eachDocument["emailid"]==emailid):
##            print("login successfully")
##            homepage(userid)
##            break
##    else:
##        print("incorrect username or password")
##while(True):
##    print("1->signup")
##    print("2->sign in")
##    print("3->exit")
##    choice=int(input("Enter your choice:"))
##    if(choice==1):
##        signup()
##    elif(choice==2):
##        signin()
##    elif(choice==3):
##        print("exit")
##        break
##    else:
##        print("invalid choice")









import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["pythonDatabase"]
mycol=mydb["login"]


def update(personid):
    print("1->update email")
    print("2-> update name")
    print("3-> update password")
    choice=int(input("Enter your choice"))
    if(choice==1):
        newEmail=input("Enter new email id")
        mycol.update_one({"_id":personid},{"$set":{"emailid":newEmail}})
def homePage(personid):
    print("1->update")
    print("2->delete")
    print("3->exit")
    choice=int(input("Enter your choice"))
    if(choice==1):
        update(personid)
    elif(choice==2):
        mycol.delete_one({"_id":personid})
    elif(choice==3):
        return 
def signup():
    print("signup")
    username=input("Enter user name")
    emailid=input("Enter email id")
    password=input("Enter password")
    confirmPassword=input("Re-enter password")
    if(password!=confirmPassword):
        return
    userDetail={"username":username,"emailid":emailid,"password":password}
    for eachDocument in mycol.find():
        if(eachDocument["emailid"]==emailid):
            break
    else:
        result=mycol.insert_one(userDetail)
        print("user registered successfully")
        personId=result.inserted_id
        homePage(personId)
def signin():
    print("signin")
    emailid=input("Enter email id")
    password=input("Enter password")
    for eachDocument in mycol.find():
        if(eachDocument["emailid"]==emailid):
            print("login successfully")
            break
    else:
        print("incorrect username or password")

while(True):
    print("1->signup")
    print("2->sign in")
    print("3->exit")
    choice=int(input("Enter your choice"))
    if(choice==1):
        signup()
    elif(choice==2):
        signin()
    elif(choice==3):
        print("exit")
        break
    else:
        print("invalid choice")
