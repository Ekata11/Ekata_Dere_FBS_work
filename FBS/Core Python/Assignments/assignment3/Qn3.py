## to input angles of a triangle and whether triangle is valid or not.

angle1 = int(input("Enter measure of angle1 : "))
angle2 = int(input("Enter measure of angle2 : "))
angle3 = int(input("Enter measure of angle3 : "))
sum = angle1 + angle2 + angle3                   ## sum of all angles of triangle is 180

if(sum == 180):
    print("Valid Triangle")
else:
    print("Invalid Triangle")