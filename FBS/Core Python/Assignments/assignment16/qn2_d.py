#add static member discount
class Product:
    discount=0
    
    def __init__(self,pid=None,pname=None,price=0,quantity=0):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity
        print("\nProduct object created.")
    
    def __del__(self):
        print("\nProduct object is destroyed.")  
    
    def ShowProduct(self):
        print(f"\nID: {self.pid},\nName: {self.pname},\nPrice: {self.price},\nQuantity: {self.quantity}")  
        
    def ApplyDiscount(self):
        discount_price = self.price - (self.price * Product.discount)   
        print(f"Discounted price is :", discount_price)  
        return discount_price   
    
p1=Product(201,"Laptop",50000,2)   
p1.ShowProduct()
p1.ApplyDiscount() 