# multiply all items in dict

def mul_items(d):
    m=1
    for k in d:
        m*=d[k]
    return m
dict={"py":1,"DA":3,"DS":4}
print("Multiplication is =", mul_items(dict))
    