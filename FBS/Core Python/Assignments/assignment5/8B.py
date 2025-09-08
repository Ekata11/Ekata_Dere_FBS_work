## N+N**2+N**3+---+N**n

N = int(input("Enter N : "))
s=0
for i in range(1,N+1):
    s = s+N**i

print(f'Sum = {s}')    