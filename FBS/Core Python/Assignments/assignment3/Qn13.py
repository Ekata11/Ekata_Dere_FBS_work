## input electricity charge and calculate total electricity bill

units = int(input("Enter Electricity Units : "))
bill = 0

if(units <= 50):
    bill = units * 0.50
elif(units<= 150):
    bill = (50 * 0.50) + (units-50)* 0.75
elif(units<=250):
    bill = (50 * 0.50) + (100 * 0.75) + (units-100)*1.20
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) (units-100)*1.50
    
    
bill = bill + (bill * 0.20)    ### additinal 20%

print(f'Total Electricity Bill is : Rs. {bill}')   