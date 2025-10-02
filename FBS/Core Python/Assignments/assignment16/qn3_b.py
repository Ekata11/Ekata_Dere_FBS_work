#distrcuctor

class Shirt:
    def __init__(self,sid,sname,type,price,size):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size
        print("Shirt is created.", self.sname)
        
    def __del__(self):
        print("Shirt is destroyed.", self.sname)    
        
           
s1=Shirt(201,"H & M","Formal",1000,"L") 
del s1
 