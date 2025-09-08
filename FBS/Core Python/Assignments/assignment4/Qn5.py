## fibonacci series upto n

n = int(input("Enter n : "))
a,b = 0,1
for i in range(n):
    print(a, end=' ')
    a,b = b, a+b
    
    
n = int(input("Enter how many fibonacci numbers you want:"))
a = -1
b = 1
for i in range(n):
    c = a+b
    print(c, end = ' ')  
    a=b
    b=c  