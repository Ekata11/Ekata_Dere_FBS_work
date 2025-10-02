#add static variable count and maintain count obj cretaed

class Book:
    count=0   #STATIC VARIABLE
    def __init__(self,bid=None,bname=None,price=None,author=None):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
        Book.count+=1
        print("Book object is created.")
        
    def __del__(self):   
        print("Book object is destroyed.") 
        
    def ShowBook(self):
        print("ID:", self.bid)
        print("Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)

b1=Book(101,"Python Basics",500,"Guido Van Rosssum")   
b1.ShowBook()
print("Total books:", Book.count) 