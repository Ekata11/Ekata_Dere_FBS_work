#3..check if given key exists in dict or not


def check_key(dict,key):
    
    for i in dict:
        if i==key:
            return True
    return False  

dict1= {"name":"John","age":23}  
key_to_check="name"
print(check_key(dict1,key_to_check))  










