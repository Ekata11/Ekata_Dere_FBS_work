# find sum of digits

def sum_of_digits(n):
    if n == 0:
        return 0
    return(n%10)+ sum_of_digits(n//10)
n=int(input("Enter num1: "))

print("Sum of digits is :", sum_of_digits(n))
sum_of_digits(n)