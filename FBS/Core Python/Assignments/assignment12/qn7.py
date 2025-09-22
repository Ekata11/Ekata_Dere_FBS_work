# cal length of str without using lib fn

def length_str(str1):
    l=0
    h=0
    for ch in str1:
        if ('a'<=ch<='z') or ('A'<=ch<="z") or (" "):
            l+=1
       
    print("Length of string is : ", l) 
     
text="Ekata Santosh Dere"   
print("Original String is :", text)  
length_str(text)    
    
    
    
    

            
    
    