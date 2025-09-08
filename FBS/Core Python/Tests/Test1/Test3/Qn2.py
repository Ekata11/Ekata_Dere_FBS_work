## calculate sum of series

n = int(input("Enter n :"))

s = 0

for i in range(1,n+1):
    fact =1
    for j in range(1,i+1):
     fact = fact * j
    s = s+(i/fact)
print(f"sum = {s}")   


