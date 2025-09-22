# create new list from exixting onece and new list is cube of each no

def cube_list(li):
    n=0
    for ele in li:
        n+=1
    new = [0]*n
    for i in range (n):
        new[i] = li[i]* li[i] * li[i]  
    return new

li=[13,33,45,66,88]     
print("Cubes = ", cube_list(li))






