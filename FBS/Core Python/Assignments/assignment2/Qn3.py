## feet ,inch into m and cm

feet = int(input("Enter distance in feet : "))
inch = int(input("Enter distance in inches : "))

total_inch = (feet * 12) + inch
cm = total_inch * 2.54
m = cm // 100
cm = cm % 100

print(f'{m}m and {cm}cm')

