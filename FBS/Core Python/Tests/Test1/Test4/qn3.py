# print patternn

def z_pattern(n):
    print('*' * n)               #top side
    
    i=10              # for that diagonal
    while i>0:
        print("  " * i + "*")
        i-=1
        
    print("*" * n + "*")            #bottom
  
z_pattern(20)    