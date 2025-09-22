# to create 3lists of no ,their squares and cubes

def num_sq_cube(li):
    n = 0
   
    sq = [0]*n
    cb = [0]*n
    
    for i in range(n):
        sq[i] = li[i] * li[i]     
        cb[i] = li[i] * li[i]  * li[i] 
    return li, sq, cb

li = [3,5,7,8,9]  
num, sq, cb = num_sq_cube(li)  

print("Numbers : ", num)
print("Squares : ", sq)
print("Cubes : ", cb)

          
    
