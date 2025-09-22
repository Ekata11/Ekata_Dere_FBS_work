# remove nth index charcter from non empty str

def remove_char(s,n):
    res=" "
    i=0
    for ch in s:
        if i!=n:
            res += ch
        i += 1
    return res

st = "Ekata"
print(remove_char(st,2))        