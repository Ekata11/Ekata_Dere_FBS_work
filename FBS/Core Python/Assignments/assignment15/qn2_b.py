#2. Destructor

class Product:
    def __init__(self,pid,pname,price,quality):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quality=quality
        print(f"[Product Created] {self.pname}")
        
    def __del__(self):
        print(f"[Product Deleted] {self.pname}")    
        
p1=Product(201,"Laptop",50000,"High")   
del p1    