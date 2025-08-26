##time hh ,mm,ss

hour = int(input("Enter hours : "))
min = int(input("Enter minutes : "))
sec = int(input("Enter seconds : "))

total_seconds = (hour * 3600) + (min * 60) + sec

print(f'Total seconds : {total_seconds} sec')