# given 2 sets of no,write code to find missing no in the sec set as compared to first and

def missing(s1,s2):
    a=[]
    b=[]
    for i in s1:
        if i not in s2:
            [a]+=i
    for j in s2:
        if j not in s1:
            [b]+=j
    return a,b

print(missing([1,2,3,4],[3,4,5,6]))                