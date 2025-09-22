# craete a duplicate of an existing list.it should not point to same list

list1 = [10,20,30,40,50]
list2 = []

for ele in list1:
    list2 = list2 + [ele]
 
 
list1[0] = 11    
print("List1 : ", list1)  
print("List2 : ", list2)  

