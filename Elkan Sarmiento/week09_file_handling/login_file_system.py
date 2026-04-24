def register_eas():
    username_eas = input("Enter username: ")
    password_eas = input("Enter password: ")
    with open("users.txt", "a") as file_eas:
        file_eas.write(username_eas + "," + password_eas + "\n")
    print("Registration successful!")

def login_eas():
    username_eas = input("Enter username: ")
    password_eas = input("Enter password: ")
    try:
        with open("users.txt", "r") as file_nbs:
            for line_eas in file_nbs:
                stored_user_eas, stored_pass_eas = line_eas.strip().split(",")
                if username_eas == stored_user_eas and password_eas == stored_pass_eas:
                    print("Login successful!")
                    return
        print("Invalid credentials!")
    except FileNotFoundError:
        print("No users registered yet!")

def main_eas():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice_eas = input("Enter choice: ")
        
        if choice_eas == "1":
            register_eas()
        elif choice_eas == "2":
            login_eas()
        elif choice_eas == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main_eas()
