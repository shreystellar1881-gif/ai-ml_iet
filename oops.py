class Books:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = "available"

    def borrow_book(self):
        if self.status == "available":
            print("The book can be borrowed")
          
        else:
            print("The book is already borrowed")

    def return_book(self):
        if self.status == "borrowed":
            
            print("Book returned")
        else:
            print("Book is not borrowed")
     

class Members:
    def __init__(self,member_id,name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

        def borrow_book(self,book):
            if book.status == "available":
              
               self.borrowed_books.append(book)
               print("Book borrowed")

            else:
                print("Book not available")

        def return_book(self,book):
            if book in self.borrowed_books:
                book.status == "available"
            
                self.borrowed_books.remove(book)
                print("Book returned")

            else:
                print("Book not returned")

class Library:
    def __init__(self):
        self.book = []
        self.member = []

    def add_book(self,book):
            self.book.append(book)
            print("Book added")

    def add_member(self,member):
            self.member.append(member)
            print("Member added")

    def remove_book (self,book_id):
        for book in self.book:
            if book.book_id == book_id:
                self.books.remove(book)
                print("Book removed ")
                return
        print("Book not found") 

    def search_book(self, title):
        for book in self.book:
            if book.title == title:
                print(book)
                return book
        print("Book not found")

    def remove_member (self,member_id):
        for member in self.member:
            if member.member_id == member_id:
                self.member.remove(member)
                print("Member removed ")
                return
        print("Member not found")

    def search_member (self, name):
        for member in self.member:
            if member.name == name:
                print(member)
                return member
        print("Member not found")

    def display_books(self):
        for book in self.book:
            print(book)

    def display_members(self):
        for member in self.member:
            print(member)
        
def menu():
    print("1. Add book")
    print("2. Display books")
    print("3. Add member")
    print("4. Display Members")
    print("5. Search Book")
    print("6. Search member")
    print("7. Exit")

lib = Library()

lib.add_book(Books(10, "Harry Potter", "Jk Rowling"))
lib.add_book(Books(12, "Atomic Habits", "James Clear"))
lib.add_member(Members(1, "Tony"))
lib.add_member(Members(2, "Shawn"))

while True:
    menu()
    choice = input("Choice number: ")

    if choice == "1":
        id = input("Book ID : ")
        title = input ("Title: ")
        author = input("author: ")

        lib.add_book(Books(id,title,author))

    elif choice == "2":
        lib.display_books()

    elif choice == "3":
        name = input("name:" )
        memberid = input("Member ID: ")
        lib.add_member(Members(name, memberid))

    elif choice == "4":
        lib.display_members()

    elif choice == "5":
        bname = input("book name: ")
        lib.search_book(bname)

    elif choice == "6":
        mname = input("member name: ")
        lib.search_member(mname)

    elif choice == "7" :
        break

    else:
        print("error")


    


    



