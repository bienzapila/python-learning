class LibraryBook:
    library_name = "Python Library"
    total_books = 0

    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.is_available = True
        self.reader = 'Нет'

        LibraryBook.total_books += 1

    def borrow(self, reader):
        if self.is_available:
            self.is_available = False
            self.reader = reader
            print(f'{self.name}: книга выдана читателю {self.reader}')
        else:
            print(f'{self.name}: книга уже выдана')

    def return_book(self):
        if not self.is_available:
            print(f'{self.name}: книга возвращена читателем {self.reader}')
            self.is_available = True
            self.reader = 'Нет'
        else:
            print(f'{self.name}: книга уже находится в библиотеке')

    def show_info(self):
        if self.is_available:
            print(f'''Книга "{self.name}" | Автор: {self.author} | Библиотека: {self.library_name} | Статус: доступна''')
        else:
            print(f'''Книга "{self.name}" | Автор: {self.author} | Библиотека: {self.library_name} | Статус: выдана читателю {self.reader}''')

    def set_personal_library(self, library_name):
        self.library_name = library_name

    
book1 = LibraryBook(input(), input())
book2 = LibraryBook(input(), input())

book1.borrow(input())
book2.borrow(input())
book2.borrow('Example')

LibraryBook.library_name = input()
book1.set_personal_library(input())

book1.return_book()

book1.show_info()
book2.show_info()

print(f'Всего книг: {LibraryBook.total_books}')