from db import Database
from user import User
 
class Logic:
    def __init__(self):
        self.db = Database()
 
    def adduserlogic(self, name, age):
        user_obj = User(name, age)
        return self.db.adduser(user_obj)
 
    def getalluserlogic(self):
        return self.db.getallusers()
 
    def cleanupresources(self):
        return self.db.cleanup()
 

if __name__ == '__main__':
    logic = Logic()
   
    print("Adding users...")
    if logic.adduserlogic("A", 26):
        print("User A added successfully.")
    if logic.adduserlogic("B", 25):
        print("User B added successfully.")
   

    users = logic.getalluserlogic()
    for user in users:
        print(f"Name: {user.name}, Age: {user.age}")
   
