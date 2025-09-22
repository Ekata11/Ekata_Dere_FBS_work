# remove char of odd ind values in a str

def remove_char(str1):
    res = ""
    i=0
    for ch in str1:
        if i %2!=0:
            res +=ch
        i+=1    
    return res

st="BANANA"    
print("New string is :", remove_char(st))  
 