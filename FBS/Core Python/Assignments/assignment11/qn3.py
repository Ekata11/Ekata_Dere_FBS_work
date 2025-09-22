#sort list according to sec ele in sublist

def sec_ele(li):
    n=0
    for ele in li:n+=1
    for i in range(n):
        for j in range(i+1,n):
            if li[i][1]>li[j][1]:
                li[i],li[j]=li[j],li[i]
        
    return li
li1=([[4,1],[3,7],[9,2],[3,4]])
print(sec_ele(li1))            
sec_ele(li1)            