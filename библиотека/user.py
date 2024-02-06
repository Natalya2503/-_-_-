# User (Пользователь):
# Свойства: имя, ID, список взятых книг.
# Методы: вывод информации о пользователе, взятие/возврат книги
from book import Book
class User:
    __slots__ = ('__user', '__ID', 'list_books' )
    def __init__(self, user: str, ID: int, list_books: list):
        if type(user) != str:
            raise 'name is not string'
        if type(ID) != int:
            raise 'ID must be int'
       
       
        self.__user = user
        self.__ID = ID
        self.list_books = []
    
    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self, user):
        self.__user = user
    
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID):
        self.__ID = ID
    
    def display_info(self):
         print(f'Имя: {self.__user} \nID: {self.__ID} \nСписок книг пользователя: {self.list_books}')
    
    def return_book(self, book):
        if book in self.list_books:
          self.list_books.remove(book)
          print(f'Книга {book} вовращена в библиотеку \nСписок книг: {self.list_books}')
          
    def take_book(self, book):
        self.list_books.append(book)
        print(f'Книга {book} взята на прочтение \nСписок книг: {self.list_books}')

book = Book('Гроза', 'А.Островский', 1982, 'драма', 5)
user1 = User('Виктор Иванов', 678, '')
user1.display_info()
user1.take_book(book)

print('--------------')
user1.display_info()
user1.return_book(book)







