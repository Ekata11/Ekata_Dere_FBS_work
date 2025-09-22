# count no of lowercase char in a str

def lowercase(str1):
    l =0
    for ch in str1:
        if 'a' <= ch <= 'z':
            l+=1
            
    print("Lowercase : ", l)   
    
lowercase("Ekata Santosh Dere")         