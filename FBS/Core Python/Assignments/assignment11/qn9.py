# create 3 lists of no,therir square and cubes

def num_sq_cb(li):
    n = 0
    for i in li:
        n += 1
        
    num = [0]*n  
    sq = [0]*n
    cb = [0]*n
    
    for i in range(n):
        num[i]=li[i]
        sq[i]=li[i]*li[i]
        cb[i]=li[i]*li[i]*li[i]
        
    return num,sq,cb    
li=[1,3,5,7,9]
n,s,c = num_sq_cb(li)
print("Numbers : ", n)
print("Squares : ", s)
print("Cubes : ", c)
