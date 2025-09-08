# check if no is perfect no
# a num that equal the sum of its divisors excluding itself if no. 6 = 1,2,3   sum== 6

n = int(input("Enter a Number: "))
s=0
for i in range(1,n):
    if n % i ==0:
        s+=i
if s==n:
    print("Perfect number")
else:
    print("Not a perfect number")