## check if 3digit no. is palindrome or not
## 121 == 121
## reverse no is same as original no.

num = int(input("Enter 3digit Number : "))
rev = (num % 10 ) * 100 + (num //10 %10) * 10 + (num // 100)

if num == rev:
    print("Palindrome Number")
else:
    print("Not a palindrome")
    