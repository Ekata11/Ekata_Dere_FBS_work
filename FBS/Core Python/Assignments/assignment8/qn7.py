#sum of digitd of no

def sum_of_digits(n):
    total = 0 
    
    #first count how many digits are in n
    temp = n
    digits = 0
    while temp>0:
        digits += 1
        temp //= 10
        
    #use for loop to extract digits    
    for i in range(digits):
        digit = n%10
        total += digit
        n//=10
    return total

num = int(input("Enter a number: "))   
print("Sum of digits = ", sum_of_digits(num)) 