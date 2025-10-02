#3 sum all items in dict

def sum_dict(d):
    s=0
    for k in d:
        s=s+d[k]
    return s

my_dict={"py":1,"DA":2}
print("Sum is:",sum_dict(my_dict))    