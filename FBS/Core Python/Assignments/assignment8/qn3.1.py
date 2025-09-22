# additition of no upto n

def add(n):
    total = 0
    for i in range(1,n+1):
        total = total + i
    return total

num = int(input("Enter a number = "))   
print("Sum from 1 to",num,"=",add(num)) 


        