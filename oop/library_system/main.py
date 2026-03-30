from models import *
from data import *

def main():
    library = Library()

    for id, val in books_data.items():
        book = Book(id, val['title'], val['author']) 
        library.add_book(book)
    
    library.display_books()



if __name__ == "__main__":
    main()