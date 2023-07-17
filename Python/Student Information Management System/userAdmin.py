from users import Users
import json
class UserAdmin(Users):
    def __init__(self,user_id,user_email,user_password,user_role="AD",user_status="Active"):
        super().__init__(user_id,user_email,user_password,user_role,user_status)

    def __str__(self):
        return f"{self.user_id},{self.user_email},{self.user_password},{self.user_role},{self.user_status}"
    
    @staticmethod
    def list_all_users():
        with open('users.txt','r') as file:
            for line in file:
                user = json.loads(line)
                print(user)

    @staticmethod
    def list_all_units():
        with open("unit.txt","r") as file:
            for line in file:
                unit = json.loads(line)
                print(unit)
    
    @staticmethod
    def enable_disable_user(email):
        if(Users.check_useremail_exists(email)):
            with open("users.txt","r") as file:
                data = [json.loads(line) for line in file]

            for user in data:
                if user["user_email"] == email:
                    if user["user_status"] == "active":
                        user["user_status"] = "deactive"
                    else:
                        user["user_status"] = "active"
            with open("users.txt","w") as file:
                for user in data:
                    file.write(json.dumps(user)+"\n")
            print("User status changed")
        else:
            print("User doesn't exists")

    @staticmethod
    def add_user(user_obj):
        if(Users.check_useremail_exists(user_obj.user_email) == False):
            with open("users.txt","a") as file:
                file.write(json.dumps(user_obj.__dict__)+"\n")
            print("User added successfully")
        else:
            print("User Email already exists")

    @staticmethod
    def delete_user(email):
        if(Users.check_useremail_exists(email)):
            with open("users.txt","r") as file:
                data = [json.loads(line) for line in file]
            with open("users.txt","w") as file:
                for user in data:
                    if(user['user_email'] != email):
                        file.write(json.dumps(user)+"\n")    
            print("User deleted successfully")
        else:
            print("Users doesn't exists")
