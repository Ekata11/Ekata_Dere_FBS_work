# 1-100 in snkaes and ladder pattern

def union_li(li1,li2):
    res = []
    for i in li1:
        for j in li2:   
            if i !=j or i ==j:
                res += [i]
            
    return res

li1=[1,4,5,6,7]
li2=[2,3,4,5]
print("Intersection of li1 and li2 : ", union_li(li1,li2))