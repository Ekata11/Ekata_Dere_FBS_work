# sum of odd no betwn 1 to n

def oddNo(n):
    s = 0
    print("Odd Numbers between 1 and", n, ":")
    for i in range(1,n+1):
        if(i%2 != 0):
            print(i)
            s = s+i
    print("Sum of odd numbers =", s)        
    
    
n = int(input("Enter n : "))  
oddNo(n)
