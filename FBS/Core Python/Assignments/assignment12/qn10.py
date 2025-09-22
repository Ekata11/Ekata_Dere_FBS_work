# take in 2 str and display the larger str

def larger_str(str1,str2):
    s1=s2=0
    for ch in str1:
        s1+=1
    for ch in str2:
        s2+=1    
    if s1 > s2:
        print("str1 is larger")
    elif s2 >s1:
        print("str2 is larger")  
    else:
        print("Both are equal")      
            
st1 = "Ekata"        
st2 = "Neha"   
larger_str(st1,st2) 

        
        
        
        
        
        
        
        
        
        
        