## roots of quadratic eqn

a=float(input("Enter coefficient a : "))
b=float(input("Enter coefficient b : "))
c=float(input("Enter coefficient c : "))

D = b**2 - 4*a*c

if D >0:
    root1 = (-b + D**0.5)/2*a
    root2 = (-b - D**0.5)/2*a
    print("Root 1:" , root1)
    print("Root 2:" , root2)
    
if D <0:   #Two real and distinct roots
    root1 = (-b + D**0.5)/ (2*a)
    root2 = (-b - D**0.5)/ (2*a)
    print("Root 1:" , root1)
    print("Root 2:" , root2)  
    
elif D == 0:  #One Real root
    root = (-b) / (2*a)
    print("Root :" , root)
    
else:      #complex roots
    real_part = -b / (2 *a)
    i_part = (D**2) / (2*a)
    print(f'Root 1 : {real_part} + {i_part} i') 
    print(f'Root 2 : {real_part} + {i_part} i')     
    
 