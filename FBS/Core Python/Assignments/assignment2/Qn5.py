## total salary based on da = 10% ,ta = 12%, hra=15% of basics

basic_salary = int(input("Enter basic salary : "))

da = basic_salary * 10/100
ta = basic_salary * 12/100
hra = basic_salary * 15/100

total_salary = basic_salary + da+ta+hra

print(f'Total salary of employee is {total_salary}')