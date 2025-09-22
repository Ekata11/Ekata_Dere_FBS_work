# find larger str

def larger(s1,s2):
    
    l1=0
    for i in s1:
        l1+=1
    
    l2=0    
    for j in s2:
        l2+=1
    if l1 > l2:
        return s1
    else:
        return s2
 
str1='Ekata'  
str2='Dere'
print(larger(str1,str2))      
            