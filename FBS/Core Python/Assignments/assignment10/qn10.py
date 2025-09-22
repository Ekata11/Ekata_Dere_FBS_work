# remove all occurence of given ele in list

def occurence(li,ele):
    res=[]
    for i in li:
        if i != ele:
            res += [i]
    return res    
    
li = [1,2,3,2,2,4,5,2]
print("Original List = ", li)
print("New list = ",occurence(li,2))
        