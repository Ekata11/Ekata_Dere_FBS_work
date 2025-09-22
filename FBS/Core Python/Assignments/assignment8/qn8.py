##  to reverse a no

def reverseNo(num):
    
     for i in range(3):
        rev = (num%10)*100 + (num//10%10)*10 + (num//100)
     if num == rev:
        print(f'{num} is a reverse number. ')
       
        
num = int(input("Enter a number = "))   
reverseNo(num)


