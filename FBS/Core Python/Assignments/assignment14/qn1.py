#find elements in given set that are not in another set

def ele_set(s1,s2):
    return s1-s2

print(ele_set({1,2,3,4},{3,4,5,6,7}))