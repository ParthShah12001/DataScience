from users import Users
from unit import Unit
from userAdmin import UserAdmin
from userTeacher import UserTeacher
from userStudent import UserStudent

def login():
    # Implement the login functionality
    # Return the logged-in user object or None if login fails
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    return Users.login(email,password)

def main_menu():
    while True:
        print("Main Menu")
        print("1. Login")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user = login()
            if user:
                if user["user_role"] == "AD":
                    user_admin_menu(user)
                elif user["user_role"] == "TA":
                    user_teacher_menu(user)
                elif user["user_role"] == "ST":
                    user_student_menu(user)
        elif choice == "2":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

def user_admin_menu(user):
    while True:
        print("User Admin Menu")
        print("1. Search User")
        print("2. List All Users")
        print("3. List All Units")
        print("4. Enable disable user")
        print("5. Add user")
        print("6. Delete user")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Implement the search user functionality
            user_email = input("Enter email id of the user you want to search")
            if(UserAdmin.search_for_user(user_email)):
                print(UserAdmin.search_for_user(user_email))
            else:
                print("User Not found")
        elif choice == "2":
            # Implement the list all users functionality
            UserAdmin.list_all_users()
        elif choice == "3":
            # Implement the list all units functionality
            UserAdmin.list_all_units()
        elif choice == "4":
            email = input("Enter email: ")
            UserAdmin.enable_disable_user(email)
        elif choice == "5":
            user_id = Users.generate_user_id()
            user_email = input("Enter email id: ")
            user_password = input("Enter password: ")
            user_role = input("Enter ST for Student and TA for Teacher: ")
            user_status = "active"
            if user_role == "ST":
                user = UserStudent(user_id,user_email,user_password,user_role,user_status,enrolled_units = {})
                UserAdmin.add_user(user)            
            elif user_role =="TA":
                user = UserStudent(user_id,user_email,user_password,user_role,user_status,teach_units = [])
                UserAdmin.add_user(user)
        elif choice == "6":
            email = input("Enter email of the user you want to delete: ")
            UserAdmin.delete_user(email)
        elif choice == "7":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def user_teacher_menu(user):
    obj = UserTeacher(**user)
    while True:
        print("User Teacher Menu")
        print("1. List teach units")
        print("2. Add new unit")
        print("3. Delete a unit")
        print("4. List enrolled students is a unit")
        print("5. Score details of a unit")
        print("6. Logout")
        choice = input("Enter your choice: ")

        if choice =="1":
            obj.list_teach_unit()
        elif choice == "2":
            unit_id = Unit.generate_user_id()
            unit_code = input("Enter unit code: ")
            unit_name = input("Enter unit name: ")
            unit_capacity = int(input("Enter unit capacity: "))
            unit = Unit(unit_id,unit_code,unit_name,unit_capacity)
            obj.add_teach_unit(unit)
        elif choice == "3":
            unit_code = input("Enter unit code you want to delete: ")
            obj.delete_teach_unit(unit_code)
        elif choice == "4":
            unit_code = input("Enter unit code: ")
            obj.list_enrolled_students(unit_code)
        elif choice =="5":
            unit_code = input("Enter unit code")
            obj.unit_avg_min_max_score(unit_code)
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid choice")

def user_student_menu(user):
    obj = UserStudent(**user)
    while True:
        print("User Teacher Menu")
        print("1. List available units")
        print("2. List enrolled unit")
        print("3. Enrol a unit")
        print("4. drop a unit")
        print("5. Check score for a unit")
        print("6. Logout")
        choice = input("Enter your choice: ")

        if choice=="1":
            obj.list_available_units()
        elif choice == "2":
            obj.list_enrolled_units()
        elif choice == "3":
            unit_code = input("Enter unit code you want to enrol: ")
            obj.enrol_unit(unit_code)
        elif choice == "4":
            unit_code = input("Enter unit code you want to drop: ")
            obj.drop_unit(unit_code)
        elif choice == "5":
            unit_code = input("Enter unit code")
            obj.check_score(unit_code)
        elif choice=="6":
            print("logging off...")
            break

if __name__ == "__main__":
    main_menu()
