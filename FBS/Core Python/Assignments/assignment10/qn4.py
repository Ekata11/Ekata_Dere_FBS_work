# reverse list

def reverse_list(li):
    n=0
    for ele in li:
        n+=1
    rev = [0] * n
    for i in range(n):
        rev[i] = li[n-1-i]
    return rev

li = [10.20,30,40,50]  
print("Reverse list is : ",reverse_list(li))      