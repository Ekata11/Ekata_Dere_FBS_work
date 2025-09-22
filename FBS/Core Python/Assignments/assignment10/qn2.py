# find max and min ele in list


def max_min(li):
    maximum = li[0]
    minimum = li[0]
    for i in li:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
    return maximum, minimum
        
li = [20,90,65,88,22]
max, min = max_min(li)
 
print("Max element:",  max)   
print("Min element:", min)            
