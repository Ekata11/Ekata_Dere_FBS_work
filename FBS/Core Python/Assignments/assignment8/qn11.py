## armstrong or not

def checkArmstrong(num):
    
    sum_digits = 0
    for i in range(3):
        digit = (num // 10**i) % 10
        cube = digit * digit * digit
        sum_digits = sum_digits + cube
        
    if sum_digits == num:
        print(num, "is an Armstrong Number")  
    else:
        print(num, "is not an Armstrong Number")  
        
n = int(input("Enter 3 digit number : "))    
checkArmstrong(n)    
       
            
    