
# ShowBook

class Book:
    def __init__(self,bid,bname,price,author):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
        print(f"[Book created] {self.bname}")
        
    def ShowBook(self):
        print("\n----Book Details----")
        print("ID :", self.bid)
        print("Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)
        
    def __del__(self):
        print(f"\n[Book Deleted] {self.bname}")
        
b1=Book(101,"Python Basics",500,"Guido Van Rossum") 
b1.ShowBook()
del b1               
