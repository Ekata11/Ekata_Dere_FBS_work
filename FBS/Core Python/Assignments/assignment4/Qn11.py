# check if no is strong no
# sum of factorials of digits is a number itself. 145 = 1! +4! +5! = 145

n = int(input("Enter a number : "))
num = n
s = 0

for d in str(n):
    fact = 1
    for i in range(1, int(d)+1):
        fact *= 1
    s += fact    

if s == num:
    print("Strong number")  
else:
    print("Not strong number")  