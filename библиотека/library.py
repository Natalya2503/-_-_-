



from book import Book
from user import User
class Library:
    __slots__ = ('_book_list', '_list_users')
    def __init__(self):
        self._book_list = list()
        self._list_users = list()
    

    @property
    def book_list(self):
        return self._book_list
    @book_list.setter
    def book_list(self, book_list):
        self._book_list = book_list
    
    @property
    def list_users(self):
        return self._list_users
    @list_users.setter
    def list_users(self, list_users):
        self._list_users = list_users
    
    def add_books(self, book):
        self._book_list.append(book)
    def __str__(self):
        return f'Добавлена книга {book}'

    def deletion_books(self, book):
        self._book_list.remove(book)
        # print(f'Удалена книга {book}')
    
    def user_registration(self, user):
        self._list_users.append(user)
        # print(f'{user} зарегистрирован')
    
    def deletion_users(self, user):
        self._list_users.remove(user)
        # print(f'{user} удалён')
    
    def issuance_book(self, book, user):
        if book in self._book_list and user in self._list_users:
            self._book_list.remove(book)
            user.list_books.append(book)
            # print(f'{user} взял {book}')

    def return_books(self, book, user):
        if book in user.list_books:
            user.list_books.remove(book)
            self._book_list.append(book)
            # print(f'{user} вернул {book}')
    


    def show_list_book(self):
        print(f'Список доступных книг: {str(self._book_list)}')

library = Library()
book = Book('Гроза', 'А.Островский', 1982, 'драма', 5)
book1 = Book('Война и мир', 'Л.Толстой', 1965, 'роман-эпопея', 10)
library.add_books(book)
library.add_books(book1)
print(f'Добавлена книга {book}')
library.deletion_books(book)
library.deletion_books(book1)
print(f'Удалена книга {book}')
user = User('Виктор Иванов', 678, '')
user1 = User('Нина Васильева', 456, '')
library.user_registration(user)
library.user_registration(user1)
print(f' зарегистрирован {user}')
library.deletion_users(user)
library.deletion_users(user1)
print(f' удалён {user}')
library.issuance_book(book, user1)
library.issuance_book(book1, user)
print(f'{user1} взял книгу {book} ')
library.return_books(book, user1)
library.return_books(book1, user)
print(f'{user1} вернул книгу {book}')
library.show_list_book()
    


    
