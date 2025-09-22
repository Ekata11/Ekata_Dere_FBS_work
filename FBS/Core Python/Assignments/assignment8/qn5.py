# sum of prime no betwn 1 to n

def primeNo(n):
    print("Prime numbers between 1 and", n, ":")
    total = 0
    
    for num in range(2,n+1):
        s=0
        for i in range(1, num+1):
            if(num%i==0):
                s = s+1
                
        if s==2:        
            print(num)
            total = total + s
            
n = int(input("Enter n : "))  
primeNo(n)              
            
        
        
        
        
        
        
