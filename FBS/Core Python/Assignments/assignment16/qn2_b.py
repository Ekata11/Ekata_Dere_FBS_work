#Distructor

class Product:
    def __init__(self,pid,pname,price,quality):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quality=quality
        print("Product is created.",self.pname)
        
    def __del__(self):
        print("Product is deleted.",self.pname)     
        
p1=Product(101,"Laptop",50000,"High") 
del p1
 
       
       
       
       
       
       
        