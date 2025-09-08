

for i in range(1,6):
    for j in range(6-i-1):
        print('  ',end=' ')
    for j in range(1,2*i)  :
        print(chr(64+j),end='  ')  
    print()  
    
 