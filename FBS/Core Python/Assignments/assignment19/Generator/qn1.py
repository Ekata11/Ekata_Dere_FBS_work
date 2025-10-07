
def fib(n):
    a,b=0,1
    for x in range(n):
        yield a
        a,b=b,a+b
    
print(list(fib(10)) )   