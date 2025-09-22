# to remove duplicates from list


def remove_duplicates(li):
    result = []
    for i in li:
        for j in result:
            if i==j:
                break        
        else:
            result = result+[i]
    return result  

           
li = [20,10,34,44,20,10]
print("Original list is : ", li)
print("New list is : ", remove_duplicates(li))

