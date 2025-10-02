#3.ShowBook

class Product:
    def __init__(self,pid,pname,price,quality):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quality=quality
        print(f"[Product Created] {self.pname}")
        
    def ShowBook(self):
        print("\n ---Product Details---") 
        print("ID:", self.pid)   
        print("Name:", self.pname)
        print("Price:", self.price)
        print("Quality:", self.quality)
        
    def __del__(self):
        print(f"\n[Product Deleted] {self.pname}")    
        
p1=Product(201,"Laptop",50000,"High") 
p1.ShowBook() 
del p1 
    