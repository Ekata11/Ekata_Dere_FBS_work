#for each size of shirt price shold chnage by 10%.use static concept
#eg if shirt price is 1000 then small price =1000,mid=1100,l=1200 and xl=1300

class Shirt:
    
    size_factor={"small":1.0, "medium":1.1, "large":1.2, "XL":1.3}
    
    def __init__(self,sid=None,sname=None,stype=None,price=0,size="small"):
        self.sid=sid
        self.sname=sname
        self.stype=stype
        self.price=price
        self.size=size
        
    def __del__(self):
        print(f"Shirt object with id {self.sid} destroyed") 
        
    def showShirt(self):
        final_price=self.price* Shirt.size_factor.get(self.size, 1.0)  
        print(f"Shirt ID: {self.sid}, Name: {self.sname}, Type: {self.stype}," f"Base Price: {self.price}, Size: {self.size}, Final Price: {final_price}")   
        
s1=Shirt(301,"Paymond", "Formal", 1000,"small") 
s2=Shirt(302,"Arrow", "Casual", 1000,"medium")
s3=Shirt(303,"Peter England", "Formal", 1000,"large")
s4=Shirt(304,"Levis", "Denim", 1000,"xlarge") 

s1.showShirt()
s2.showShirt()
s3.showShirt()
s4.showShirt()
       