# Sum of 1! + 2! + 3! + ....... n!     using REcursion

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

def sum_of_series(n):
    if n==0:
        return 0
    return fact(n)+ sum_of_series(n-1)
n= int(input("Enter n: "))
print("Sum of series is : ", sum_of_series(n))
sum_of_series(n)