# create class product ==pid,pname,price,quantity
# constructor

class Product:
    def __init__(self,pid,pname,price,quality):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quality=quality
        print("Product is craeted.",{self.pname})
        
p1=Product(101,"Laptop",50000,"High") 
print("ID:", p1.pid)
print("Name:", p1.pname)
print("Price:", p1.price)
print("Quality:", p1.quality)       
        