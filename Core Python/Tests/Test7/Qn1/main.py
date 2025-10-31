
from book import Book

books={}

def add_book():
    bid=input("Enter Book Id: ")
    name=input("Enter Book Name: ")
    price=float(input("Enter Book Price: "))
    author=input("Enter Book Author: ")
    books[bid]=Book(bid,name,price,author)
    print("Book added successfully...\n")
    
def delete_book():
    bid=input("Enter Book ID to delete: ") 
    if bid in books:
        del books[bid]
        print("Book deleted successfully...\n")
    else:
        print("Book not found!\n")
           
def display_all():
    if books:
        print("\nAll Books: ")  
        for b in books.values():
            b.display()
        else:
            print("No Books available.\n")    
         
def search_book():
    bid=input("Enter Book ID to search: ")    
    if bid in books:
        print("\nBook Found: ")
        books[bid].display()
    else:
         print("\nBook Not Found.")     
         
while True:
    print("1.Add Book")  
    print("2.Delete Book")  
    print("3.Display All Books")  
    print("4.Search Book by ID")  
    print("5.Exit")  
    
    choice=input("Enter your choice: ") 
    
    if choice == '1':
        add_book()
    elif choice=='2':
        delete_book()
    elif choice=='3':
        display_all()
    elif choice=='4':
        search_book()
    elif choice=='5':
        print("Exiting...")   
        break
    else:
        print("Invalid Credentials! Try again..")    
                    