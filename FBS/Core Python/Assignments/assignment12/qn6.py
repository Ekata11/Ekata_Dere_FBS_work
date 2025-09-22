# take in a str and replace every blank space with hypen

def space_to_hypen(str1):
    res = " "
    for ch in str1:
        if ch == " ":
            res += "_"
        else:
            res += ch
    return res

print(space_to_hypen("Ekata Santosh Dere"))        
        