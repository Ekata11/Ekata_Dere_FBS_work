#concatenate 2 dict into one

def concat_dict(dict1,dict2):
    dict3={}
    
    for i in dict1:
        dict3[i]=dict1[i]
        
    for j in dict2:
        dict3[j]=dict2[j]   
        
    return dict3      
    
    
dict1={1:"Py",2:"Java"}   
dict2={3:"DS",4:"DA"} 
print(concat_dict(dict1,dict2))
