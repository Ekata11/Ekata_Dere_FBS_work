# having n no of ele in list ,find  out even and odd ele in list andcreate 2 separate list having even no,odd no

def even_odd(li) :
    even = []
    odd = []
    for x in li:
        if x % 2==0:
            even += [x]
        else:
            odd += [x]
    return even, odd

n = int(input("Enter number of elements: "))
nums = []

for i in range(n):
    ele = int(input("Enter elements : "))   
    nums += [ele]
    
ev , od = even_odd(nums)
print("Even Numbers : ", ev)  
print("Odd Numbers : ", od)  
      
    