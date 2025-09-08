## basic salary da=10,hra=15,ta=12

n = int(input("Enter Employee number: "))
total = 0

for i in range(n):
    basic_salary = int(input("Enter Basic Salary : "))
    if(basic_salary < 20000):
        da=0.10 * basic_salary
        ta=0.12 * basic_salary
        hra=01.5* basic_salary
    else:
        da=0.15 * basic_salary
        ta=0.18 * basic_salary
        hra=0.20 * basic_salary
        
    total_salary = basic_salary +da +ta+ hra
    print(f'Total salary for employee {i+1}: {total_salary : .2f}')    
    total = total +total_salary
    
print(f"\nTotal salary of all employees: {total: .2f}")    













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