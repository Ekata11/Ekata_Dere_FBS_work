#factorial upto n

def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

num = int(input("Enter a number = "))
print("Factorial of 1 to ", num, "=",fact(num))   

           
