# craete class shirt sid,sname,type,price,size
# constrctor

class Shirt:
    def __init__(self,sid,sname,type,price,size):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size
        print("Shirt is created.",self.sname)
        
           
s1=Shirt(201,"H & M","Formal",1000,"L") 
print("\nID:", s1.sname)
print("Name:", s1.sname)
print("Type:", s1.type)
print("Price:", 1000)
print("Size:", s1.size)
 