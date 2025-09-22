# count no of digitd and letters in str

def count_let_digi(str1):
    d= l=0
    for ch in str1:
        if '0' <= ch <= '9':
            d += 1
        elif('a'<=ch<='z')or('A'<= ch <= 'Z'):
            l+=1
    print("Letters :", l)
    print("Digits : ", d)
    
count_let_digi("Hello123World")
        