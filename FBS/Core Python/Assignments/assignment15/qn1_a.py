# create a class Book with members as bid,bname,price and author .  
# a] constructor... support both parameterized and parameterless  . 

class Book:
    def __init__(self,bid,bname,price,author):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
        
b1=Book(101,'Python Basics',500,"Guido Van Rossum") 
print("Book ID:", b1.bid) 
print("Book Name:", b1.bname)  
print("Price:", b1.price)   
print("Author:", b1.author) 










