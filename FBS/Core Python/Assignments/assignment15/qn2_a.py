#Q2. Create a class Product with members as pid,pname,price, and quality.
#1. Constructor

class Product:
    def __init__(self,pid,pname,price,quality):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quality=quality
        print(f"[Product Created] {self.pname}")
        
p1=Product(201,"Laptop",50000,"High")   
    
