# print all no which are divisible by m and n in list

def divisible_by(li,m,n):
    res = []
    for i in li:
        if i % m ==0 and i % n == 0 :
            res += [i]
    return res 

li = [11,45,67,88,99,78]    
print("Divisisble by 3 and 6 : ", divisible_by(li,3,6))

