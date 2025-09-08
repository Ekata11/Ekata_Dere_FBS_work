## print first n prime no

n = int(input("Enter a number : "))
num=2
count=0 

while count<n:
    for i in range(2,num):
        if(num%i == 0):
            break       
    else:
        print(num)
        count=count+1
    num = num   +1 