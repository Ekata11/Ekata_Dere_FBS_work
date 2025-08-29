## Leap year

year = int(input("Enter Year : "))

if(year%4 == 0):
    if( year%100 == 00):
        if(year%400==00):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else: 
            print(f"{year} is not a leap year.")
else:
            print(f"{year} is not a leap year.")

