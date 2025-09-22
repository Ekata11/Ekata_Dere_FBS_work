## fibonacci series using fn 

def fibonacciSeries(n):
    
    a = -1
    b= 1
    for i in range(1,n):
        c = a+ b
        print(c)
        a = b
        b = c
    
    

n = int(input("Enter n : "))  
fibonacciSeries(n) 

      

















