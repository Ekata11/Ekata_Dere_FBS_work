## print armstrong no within a given range 1 to 100
# number that equals to the sum of its digits raised to a power of num of digits      153 = 1'3 + 5'3 +3'3 == 153

start = int(input("Enter start of range = "))
end = int(input("Enter end of range = "))

for num in range(start ,end+1):
    
    temp=num
    digits=0
    for k in range(num):
        if temp==0: break
        temp = temp//10
        digits = digits+1
        
    temp=num
    s=0
    for k in range(num):
        if temp ==0:break
        d = temp%10
        s = s+d**digits
        temp //= 10
        
    if num ==s:
        print(num)        
    



