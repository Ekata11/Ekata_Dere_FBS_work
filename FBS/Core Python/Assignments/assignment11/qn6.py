#union of 2li

def union_li(li1,li2):
    res = []
    for i in li1 + li2:
        if i not in res:
            res += [i]
            
    return res

li1=[1,4,5,6,7]
li2=[2,3,4,5]
print("Union of li1 and li2 : ", union_li(li1,li2))
        
    