# print list after removing even no

def remove_even(li):
    even = []
    odd = []
    for i in li:
        if i %2==0:
            even += [i]
        else:
            odd += [i]
    return odd

list = []
od = remove_even(list)
li = [22,45,66,78,99,33]  
print("Original list : ", li)   
print("New list is : ", remove_even(li)  ) 
remove_even(li)
            
            
            
            
            
            
            
            