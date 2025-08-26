## person eligible to marry or not


gender = input("Enter gender (M/F): ")
age = int(input("Enter age: "))

if(gender == 'M' or gender == "Male" or gender== "m"):
   if(age >= 21):
       print("Eligible to marry. ")
   else:
       print("Not eligible to marry. ")
else:    
    if(age>17):
        print("Eligible to marry. ")
    else:
        print("Not eligible to marry.")
    
