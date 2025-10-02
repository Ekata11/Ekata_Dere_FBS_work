#showbook

class Product:
    def __init__(self,pid,pname,price,quality):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quality=quality
        print("Product is created.",self.pname)
        
    def __del__(self):
        print("\nProduct is deleted.",self.pname)     
        
    def ShowBook(self):
        print("\n---Product Details---")
        print("ID:", p1.pid)
        print("Name:", p1.pname)
        print("Price:", p1.price)
        print("Quality:", p1.quality)     
        
p1=Product(101,"Laptop",50000,"High") 
p1.ShowBook()
del p1
 