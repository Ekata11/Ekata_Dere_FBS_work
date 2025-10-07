
def palin_gen():
    n=1
    while True:
        if str(n) == str(n)[::-1]:
            yield n
        n+=1
        
gen = palin_gen()
for x in range(10):
    print(next(gen))
            