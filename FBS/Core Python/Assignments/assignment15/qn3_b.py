#Destructor

class Shirt():
    def __init__(self,sid,sname,type,price,size):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size
        print(f"[Shirt is created] {self.sname}")
        
    def __del__(self):
        print(f"[Shirt is not created] {self.sname}")    
        
s1=Shirt(301,"H & M","Formal",1000,"M") 
 
# print("\nShirt ID:", s1.sid)  
# print("Name:", s1.sname)
# print("Type:", s1.type)
# print("Price:", s1.price)
# print("Size", s1.size) 

del s1