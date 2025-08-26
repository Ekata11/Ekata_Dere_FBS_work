## CAPTCHA

import random
uid = "admin"
password = "12345"

u = input("Enter User Id : ")
p = input("Enter Password : ")

if(u == uid and p == password):
    num = random.randint(1000,9999)
    print(f'Random number : {num}')
    check = int(input("Enter CAPTCHA : "))
    if(check == num):
        print("Login successful.")
    else:
        print("Failed .")
else:
        print("Invalid user ID and password.")
    




