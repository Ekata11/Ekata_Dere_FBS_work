# to find second largest ele in list


def sec_largest(li):
    max = li[0]
    sec_max=li[0]


    for i in li:
        if(i > max):
            sec_max = max
            max = i
        elif(i>sec_max and i !=max):
            sec_max = i
    return sec_max        
        
    
li = [20,50,1,100,60]        
print("Max number is :",max(li))   
print("Second Max number :", sec_largest(li))     
