## days into Y,W,D of 2000days

total_days = int(input("Enter total amount of days:"))

years =  total_days // 365
days = total_days % 365

weeks = days // 7
days = days % 7

print(f'{years} Years , {weeks} Weeks and {days} Days')