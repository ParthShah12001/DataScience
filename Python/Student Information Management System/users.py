import random
import json
class Users:
    def __init__(self,user_id,user_email,user_password,user_role,user_status):
        self.user_id = user_id
        self.user_email = user_email
        self.user_password = user_password
        self.user_role = user_role
        self.user_status = user_status

    def __str__(self):
        return f"{self.user_id},{self.user_email},{self.user_password},{self.user_role},{self.user_status}"
    
    def to_json(self):
        return json.dumps(self.__dict__)

    
    def generate_user_id():
        return random.randint(10000,99999)

    @staticmethod
    def check_useremail_exists(email):
        with open('users.txt', 'r') as file:
            for line in file:
                user = json.loads(line)
                if user['user_email'] == email:
                    return True
        return False
    
    @staticmethod
    def search_for_user(email):
        with open('users.txt', 'r') as file:
            for line in file:
                user = json.loads(line)
                if user['user_email'] == email:
                    return user
        return None

    @staticmethod
    def search_in_txt(email,password):
        with open('users.txt', 'r') as file:
            for line in file:
                user = json.loads(line)
                if user['user_email'] == email and user['user_password'] == password:
                    return user
        return None

    @staticmethod
    def login(email,password):
        user = Users.search_in_txt(email,password)
        if(user and user["user_status"]=="active"):
            return user
        elif(user["user_status"]=="deactive"):
            return "Users is currently deactivated please contact admin"
        else:
            return "Invalid login credential"
