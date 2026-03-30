class Library:
    def __init__(self):
        self.book_collection = []
        self.user_list = []
    
    def add_book(self,book):
        self.book_collection.append(book)

    def register_user(self,user):
        self.user_list.append(user)
    
    def find_book(self, book_id):
        for book in self.book_collection:
            if book.id == book_id:
                return book
        return None
    
    def find_user(self, user_id):
        for user in self.user_list:
            if user.id == user_id:
                return user
        return None

    def borrow_book(self, user_id, book_id):
        user_found = self.find_user(user_id)
        book_found = self.find_book(book_id)

        if not user_found:
            print("User not found")
            return

        if not book_found:
            print("Book not found")
            return

        if not book_found.is_available:
            print("Book not available:", book_found.title)
            return

        user_found.borrow_book(book_found)
        book_found.is_available = False

        print(f'{user_found.name} borrowed {book_found.title}')
                
    def return_book(self, user_id, book_id):
        user_found = self.find_user(user_id)

        if not user_found:
            print("User not found")
            return
        
        book_found = user_found.return_book(book_id)

        if not book_found:
            print("The user has not borrowed that book")
            return
        
        book_in_library = self.find_book(book_id)
        if not book_in_library:
            print("Book not found")
            return

        book_in_library.is_available = True
        print(f'{user_found.name} returned {book_in_library.title}')

    # Note: In larger applications, display logic should be separated from business logic
    def display_books(self):
        print("--------------------------- BOOKS ---------------------------")
        print(f'{"ID":>3} | {"Author":<20} | {"Title":<30} | {"Available"}')
        print("-------------------------------------------------------------")
        for book in self.book_collection:
            status = "Yes" if book.is_available else "No"
            title = book.title[:27] + "..." if len(book.title) > 27 else book.title
            print(f'{book.id:>3} | {book.author:<20} | {title:<30} | {status}')



class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.is_available = True



class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
    
    def return_book(self, book_id):
        for book in self.borrowed_books:
            if book.id == book_id:
                self.borrowed_books.remove(book)
                return book
        return None