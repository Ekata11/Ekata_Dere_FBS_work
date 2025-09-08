## basic salary da=10,hra=15,ta=12

n = int(input("Enter Employee number: "))
total = 0


basic_salary = int(input("Enter Basic Salary : "))
for i in range(1,n+1):
    if(basic_salary < 20000):
        da=10/100 and hra=15/100
    else:
        da=15/100 and ta=18/100 and hra=20/100













basic_salary = int(input("Enter basic salary : "))

da = basic_salary * 10/100
ta = basic_salary * 12/100
hra = basic_salary * 15/100

total_salary = basic_salary + da+ta+hra

print(f'Total salary of employee is {total_salary}')

n = int(input("Enter number of students : "))

total = 0
for i in range(1,n+1):
    marks = 0
    for j in range(1,6):
        m = int(input(f"Enter marks of subject {j} for student {i} : "))
        marks += m
    percentage = (marks)/5 
    print(f'Student {i} Percentage = {percentage} %') 
    total += percentage 
    
print(f"Average percentage of students are : {total/n}%")    