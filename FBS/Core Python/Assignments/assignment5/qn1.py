## enter userid and pass . 3attempts

user_id = 'ekata'
user_pass = '2025'

for i in range(3):
    id = input("Enter User ID = ")
    password = input("Enter Password = ")
    if id == user_id and password == user_pass:
        print("Login Successful")
        break
    else:
        print("Invalid User ID and Password")
else:
    print("3 attempts over.")