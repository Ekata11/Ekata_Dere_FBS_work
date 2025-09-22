# put even and odd ele of list into 2diff lists

def even_odd(li):
    even = []
    odd = []
    for i in li:
        if i%2==0:
            even += [i]
        else:
            odd  += [i]
    return even , odd

li = [20,11,22,13,44,57,88,99,67]   
ev,od = even_odd(li)
print("Even Numbers : ", ev)        
print("Odd Numbers : ", od)    