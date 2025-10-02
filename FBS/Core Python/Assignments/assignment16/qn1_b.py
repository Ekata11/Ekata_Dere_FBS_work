#destructor

class Book:
    
    def __init__(self,bid=None,bname=None,price=None,author=None):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
        
        print("Book is created.", self.bname)
        
    def __del__(self):
        print("Book is destroyed.", self.bname)     
        
b1=Book(101,"Python Basics",500,"Guido Van Rossum")  
# print("ID:", b1.bid)   
# print("Name:", b1.bname)
# print("Price:", b1.price)
# print("Author:", b1.author)
del b1
