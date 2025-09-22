# print list after removing even no

def remove_even(li):
    res = []
    for i in li:
        if i % 2 != 0:
            res += [i]
    return res

li = [10,20,22,33,44,78]   
print("Even no are removed: ", remove_even(li))      
                 