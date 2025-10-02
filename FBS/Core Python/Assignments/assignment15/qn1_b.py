
# Destructor

class Book:
    def __init__(self,bid,bname,price,author):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
        print(f"[Book Created] {self.bname}")
        
    def __del__(self):
        print(f"[Book Deleted] {self.bname}")   
    
b1=Book(101,"Python Basics",500,"Guido Van Rossum")  

del b1  
        












           