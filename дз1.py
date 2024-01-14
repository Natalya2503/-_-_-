# задача 1
# Класс Книга должен содержать информацию о названии, авторе и жанре книги.

class Book:
    def __init__(self, author, name_book, book_genre):
     self.author = author
     self.name_book = name_book
     self.book_genre = book_genre
my_book = Book(author = 'Александр Островский', name_book = 'Гроза', book_genre = 'драма')
print(f'Моя книга: автор-{my_book.author}, название-{my_book.name_book}, жанр-{my_book.book_genre}.')



# задача 2
# Класс БанковскийАккаунт должен хранить информацию о владельце, балансе

class BankAccount:
   def __init__(self, name_user, age_user, phone_number, balance):
      self.__name_user = name_user
      self.__age_user = age_user
      self.__phone_number = phone_number
      self.__balance = balance
   def get_name_user(self):
      return self.__name_user
   def get_age_user(self):
      return self.__age_user
   def get_phone_number(self):
      return self.__phone_number
   def get_balance(self):
      return self.__balance
   def show_BankAccount(self):
      print(f'Владелец банковской карты: имя-{self.get_name_user()}, возраст-{self.get_age_user()}, телефон-{self.get_phone_number()}, баланс-{self.get_balance()}.')
user = BankAccount(name_user='Иванов Иван', age_user='36', phone_number='45678923', balance='1789$')
user.show_BankAccount()


