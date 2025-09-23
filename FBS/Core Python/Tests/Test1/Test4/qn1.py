# Factors of 12: 1,2,3,4,6,12

  

def factors(n):
    i=1
    for i in range(1,n+1) :
        if n%i==0:
            print(i,end=" ")    
        
        
factors(24)               