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
