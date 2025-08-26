## sum of 3digit

num = int(input("Enter 3digit number : "))

d1 = num % 10
num = num // 10

d2 = num % 10
num = num //10

d3 = num % 10
num = num // 10

sum = d1 + d2 + d3

print(f'Sum of 3digit number is : {sum}')
