## input all sides of a triangle and check whether triangle is valid or not.

A = int(input("Enter side1 : "))
B = int(input("Enter side2 : "))
C = int(input("Enter side3 : "))

## triangle is valid only if sum of two sides is greater than third..

if(A+B > C and B+C>A and C+A>B):
    print("Valid Triangle")
else:
    print("Invalid Triangle")