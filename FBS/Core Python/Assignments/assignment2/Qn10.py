## reverse 3digit

num = int(input("Enter 3digit Number : "))
rev = (num % 10 ) * 100 + (num //10 %10) * 10 + (num // 100)


print(f'Reverse of {num} is {rev}')