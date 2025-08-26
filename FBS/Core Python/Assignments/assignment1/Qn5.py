## comp interest

P = int(input("Enter the value of P:"))
R = int(input("Enter the value of R:"))
T = int(input("Enter the value of T:"))

compound_interest = P * (1+R/100)**T - P

print(f'The compound interest is {compound_interest}')