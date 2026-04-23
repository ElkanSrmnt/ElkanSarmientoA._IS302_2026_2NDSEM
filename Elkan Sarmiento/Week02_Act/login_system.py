correct_username_eas = "admin"
correct_password_eas = "1234"
attempts_eas = 0
while attempts_eas < 3:
    username_eas = input("Enter username: ")
    password_eas = input("Enter password: ")
    if username_eas == correct_username_eas and password_eas == correct_password_eas:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        attempts_eas += 1
if attempts_eas == 3:
    print("Account Locked")
