title=input('Title Of Book')
author=input('Name Of Author')
isbn=input('ISBN numbe please')
global list
list = [title]

class Books:

    def __init__(self, title, author, isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        # self.availability=availability
    pass
    def display_book_detail(self):
        list=list.append(title)
        print(f'Book details are Title: {title}, written by Author: {author}, book number:{isbn}')
        print(list)
    pass

inventory=[]


class Library:
    def __init__(self, inventory):
        self.inventory = inventory

    pass

    def print_inventory(self):
        pass
class Patrons:
    def __init__(self, name, identification, checked_books):
        self.name=name
        self.identification=identification
        self.checked_books=checked_books
    pass
    def add_book(self, name, inventory):
        inventory=inventory.append(name)
        print(inventory)
        pass




book1=Books(title, author, isbn)
book1.display_book_detail()

