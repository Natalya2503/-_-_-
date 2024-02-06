# Transaction (Транзакция):
# Свойства: дата, тип (выдача/возврат), книга, пользователь.
# Методы: запись транзакции, вывод информации о транзакции

from user import User
from book import Book

class Transaction:
    __slots__ = ('date', 't_ype', 'book', '_user')
    
    def __init__(self, date, t_ype, book, user):
        
        self.date = date
        self.t_ype = t_ype
        self.book = book
        self._user = user
     
    
    @property
    def user(self):
        return self._user
    @user.setter
    def user(self, user):
        self._user = user
    
    def record_transaction(self, date, t_ype, book, user):
        self.date = date
        self.t_ype = t_ype
        self.book = book
        self._user = user
    
    def display_info(self):
        print(f'Дата: {self.date} \nТип(выдача\возврат): {self.t_ype} \nКнига: {self.book} \nПользователь: {self._user}')

    
book1 = Book('Гроза', 'А.Островский', 1982, 'драма', 5)
user1 = User('Виктор Иванов', 678, '')
transaction = Transaction( '12.24.2023', 'выдача', book1, user1)
transaction.display_info() 
    
    



