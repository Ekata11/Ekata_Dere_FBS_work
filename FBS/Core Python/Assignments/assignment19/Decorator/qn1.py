
def memoize(func):
    cache={}
    def wrapper(*args):
        if args not in cache:
            cache[args]=func(*args)
        return cache[args]
    return wrapper    

@memoize
def fact(num):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
n=int(input("Enter number:"))
print("Factorial is:",fact(n))