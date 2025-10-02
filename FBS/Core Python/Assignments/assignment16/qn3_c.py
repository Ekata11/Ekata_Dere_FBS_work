#showbook

class Shirt:
    def __init__(self,sid,sname,type,price,size):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size
        print("Shirt is created.", self.sname)
        
    def __del__(self):
        print("\nShirt is destroyed.", self.sname) 
        
    def ShowBook(self):
        print("\n---Shirt Details---")   
        print("ID:", self.sid)  
        print("Name:", self.sname) 
        print("Type:", self.type) 
        print("Price:", self.price)
        print("Size:", self.size)
        
           
s1=Shirt(201,"H & M","Formal",1000,"L") 
s1.ShowBook()
del s1
 