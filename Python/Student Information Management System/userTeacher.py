from users import Users
from unit import Unit
import json
import statistics
class UserTeacher(Users):
    def __init__(self,user_id,user_email,user_password,user_role="TA",user_status="Active",teach_units = []):
        super().__init__(user_id,user_email,user_password,user_role,user_status)
        self.teach_units = teach_units

    def __str__(self):
        return f"{self.user_id},{self.user_email},{self.user_password},{self.user_role},{self.user_status},{self.teach_units}"
    
    def list_teach_unit(self):
        print(self.teach_units)

    def add_teach_unit(self,unit_obj):
        #add in unit.txt
        with open("unit.txt","a") as file:
            file.write(json.dumps(unit_obj.__dict__)+"\n")

        #add in teacher
        with open("users.txt","r") as file:
            data = [json.loads(line) for line in file]

        #editing the specific teacher
        for user in data:
            if user["user_email"] == self.user_email:
                user["teach_units"].append(unit_obj.unit_code)
        #making final write 
        with open("users.txt","w") as file:
            for user in data:
                file.write(json.dumps(user)+"\n")
        self.teach_units.append(unit_obj.unit_code)
        print("Unit added successfully")

    def delete_teach_unit(self,unit_code):
        if unit_code in self.teach_units:
            #Deleting from unit.txt
            with open("unit.txt","r") as file:
                data = [json.loads(line) for line in file]
            with open("unit.txt","w") as file:
                for unit in data:
                    if unit["unit_code"]!=unit_code:
                        file.write(json.dumps(unit)+"\n")

            #deleted from all students and teachers
            with open("users.txt","r") as file:
                data = [json.loads(line) for line in file]
            #editing student and teachers one by one
            for user in data:
                if user["user_role"] == "TA" and unit_code in user["teach_units"]:
                    user["teach_units"].remove(unit_code)
                elif user["user_role"] == "ST" and unit_code in user["enrolled_units"]:
                    user["enrolled_units"].pop(unit_code)
            #Making final write to users.txt
            with open("users.txt","w") as file:
                for user in data:
                    file.write(json.dumps(user)+"\n")
                self.teach_units.remove(unit_code)
                print("Unit deleted successfully")
        else:
            print("You are not authorized to deleted this Unit")

    @staticmethod
    def list_enrolled_students(unit_code):
        list_enrolled=[]
        #reading all data
        with open("users.txt","r") as file:
            data = [json.loads(line) for line in file]
        #sorting the list with only the students who are enrolled in the specific class
        for user in data:
            if user["user_role"] == "ST" and unit_code in user["enrolled_units"]:
                list_enrolled.append(user)
        if len(list_enrolled)!=0:
            print(list_enrolled)
        else:
            print("No student is regestered in this course")
    
    @staticmethod
    def unit_avg_min_max_score(unit_code):
        list_enrolled=[]
        score=[]
        #reading data 
        with open("users.txt","r") as file:
            data = [json.loads(line) for line in file]

        #adding data in new list in dict format with only user_email and the unit_code and marks 
        for user in data:
            if user["user_role"] == "ST" and unit_code in user["enrolled_units"]:
                list_enrolled.append({"user_email":user["user_email"],unit_code:user["enrolled_units"][unit_code]})

        #creating new list just to hold marks to easily find min and max
        for user in list_enrolled:
            score.append(user[unit_code])

        print("Average score: ",statistics.mean(score))
        max_marks = max(score)
        min_marks = max(score)
        print("Max marks")
        for user in list_enrolled:
            if  user[unit_code] == max_marks:
                print(user)
        print("Min Marks")
        for user in list_enrolled:
            if  user[unit_code] == min_marks:
                print(user)

#UserTeacher(**obj)