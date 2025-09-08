## avg marks of students


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