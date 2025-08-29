# 3 digit no.


num = int(input("Enter 3 Digit Number : "))
d1 = int(input("Enter digit1 : "))
d2 = int(input("Enter digit2 : "))
d3 = int(input("Enter digit3 : "))

if(d1 == d2*2 and d1 == (0.5*d3)):
    print("Yes, you have done it.")
else:
    print("Please try next time. ")
