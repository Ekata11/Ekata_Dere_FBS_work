# remove given key from dict

def remove_key(d,key):
    new_d={}
    for k in d:
        if k!=key:
            new_d[k]=d[k]
    return new_d

my_dict={'a':10,'b':20,'c':30}  
print("New dict:", remove_key(my_dict,'c'))      
    