# to form a new str where the first charter and last char have been ecxhaged

def swap_char(str1):
    n=0
    for char in str1:
        n+=1
    if n<=1:
        return str1
    return str1[n-1]+str1[1:n-1]+str1[0]
            
print(swap_char("HELLO"))            







