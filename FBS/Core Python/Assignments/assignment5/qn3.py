## ticket booking with discout condition

passengers = int(input("Enter number of passengers : "))
ticket = int(input("Enter ticket cost per person : "))

total = 0 
for i in range(passengers):
    age = int(input(f'Enter age of passengers {i+1} : '))
    if age < 12:
        total += ticket * 0.7       #(total = total * 1-discount)    30%
    elif age > 59:
        total += ticket*0.5         # 50%
    else:
        total += ticket
        
print(f'Total ticket amount is : {total}')        