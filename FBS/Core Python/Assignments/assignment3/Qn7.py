## check if user has entered correct userid and pass.

uid = "admin"
password = "12345"

u = input("Enter user ID : ")
p = input("Enter password : ")

if(u == uid and p == password):
    print("Valid user ID and password.")
else:
    print("Invalid user ID and password. ")
