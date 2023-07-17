from users import Users
import random
import json
class UserStudent(Users):
    def __init__(self,user_id,user_email,user_password,user_role,user_status,enrolled_units):
        super().__init__(user_id,user_email,user_password,user_role,user_status)
        self.enrolled_units = enrolled_units

    def __str__(self):
        return f"{self.user_id},{self.user_email},{self.user_password},{self.user_role},{self.user_status},{self.enrolled_units}"
    
    def list_available_units(self):
        if len(self.enrolled_units)<3:
            with open("unit.txt","r") as file:
                data = [json.loads(line) for line in file]
            for unit in data:
                if unit["unit_capacity"]>0:
                    print(unit)
        else:
            print("You have already enrolled in 3 units so can't enroll in any other units")

    def list_enrolled_units(self):
        print(self.enrolled_units)

    def check_unit(self,unit_code):
        with open("unit.txt","r")as file:
            data = [json.loads(line) for line in file]
        for unit in data:
            if unit["unit_code"] == unit_code:
                return True
        return False
    
    def enrol_unit(self,unit_code):
        if(self.check_unit(unit_code)):
            if unit_code in self.enrolled_units:
                print("You are already enrolled in this unit")
            else:
                if len(self.enrolled_units) < 3:
                    #editing in users.txt
                    with open("users.txt","r") as file:
                        data = [json.loads(line)for line in file]
                    
                    for user in data:
                        if user["user_email"] == self.user_email:
                            user["enrolled_units"][unit_code] = 0
                    with open("users.txt","w")as file:
                        for user in data:
                            file.write(json.dumps(user)+"\n")
                    
                    #editing in unit.txt
                    with open ("unit.txt") as file:
                        data = [json.loads(line) for line in file]
                    for unit in data:
                        if unit["unit_code"] == unit_code:
                            unit["unit_capacity"] -= 1
                    with open("unit.txt","w")as file:
                        for unit in data:
                            file.write(json.dumps(unit) + "\n")
                    print(f"You have successfully enrolled to {unit_code} unit")
                else:
                    print("You are already enrolled in 3 units you can't enroll in more units")
        else:
            print("Invaild unit please type in proper unit_code")
    
    def drop_unit(self,unit_code):
        if self.check_unit(unit_code):
            if unit_code in self.enrolled_units:
                #editing in users.txt
                with open("users.txt","r") as file:
                    data = [json.loads(line)for line in file]
                    for user in data:
                        if user["user_email"] == self.user_email:
                            user["enrolled_units"].pop(unit_code)
                    with open("users.txt","w")as file:
                        for user in data:
                            file.write(json.dumps(user)+"\n")
                    
                    #editing in unit.txt
                    with open ("unit.txt") as file:
                        data = [json.loads(line) for line in file]
                    for unit in data:
                        if unit["unit_code"] == unit_code:
                            unit["unit_capacity"] += 1
                    with open("unit.txt","w")as file:
                        for unit in data:
                            file.write(json.dumps(unit) + "\n")
                print(f"You have dropped {unit_code} unit")
            else:
                print("You are not enrolled in this unit")
        else:
            print("Invalid unit code please type in valid unit code")
    def check_score(self,unit_code):
        if unit_code in self.enrolled_units:
            print(unit_code +": " +str(self.enrolled_units[unit_code]))
        else:
            print("You are not enrolled in this unit")
        
    def generate_score(self,unit_code):
        if unit_code in self.enrolled_units:
            with open("users.txt","r")as file:
                data = [json.loads(line) for line in file]
            
            for user in data:
                if user["user_email"] == self.user_email:
                    user["enrolled_units"][unit_code] = random.randint(0,100)
            
            with open("users.txt","w") as file:
                for user in data:
                    file.write(json.dumps(user)+"\n")
            print("Score updated successfully")
        else:
            print("You are not enrolled in this unit")

obj = Users.login("tirth@example.com","password123")
obj = UserStudent(**obj)
obj.drop_unit("CS102")