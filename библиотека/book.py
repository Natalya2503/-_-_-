# Book (Книга):
# Свойства: название, автор, год издания, жанр, количество экземпляров.
# Методы: вывод информации о книге, уменьшение/увеличение количества экземпляров.

class Book:
    
    def __init__(self, title: str, author: str, year: int , genre: str, quantity: int):
        if type(title) != str:
            raise 'title is not string'
        if type(author) != str:
            raise 'author is not string'
        if type(genre) != str:
            raise 'genre is not string'
        self.title = title
        self.author = author
        self.year = self.valid_value(year)
        self.genre = genre
        self.quantity = self.valid_value_quantity(quantity)
    @staticmethod
    def valid_value(year):
        if type(year) != int:
            raise 'год  должен быть числом'
        if year < 1445 and year > 3000:
            raise 'год издания указан неверно'
        return year
    @staticmethod
    def valid_value_quantity(quantity):
        if type(quantity) != int:
            raise 'количество должно быть числом '
        if quantity < 0:
            raise 'количество не может быть меньше 0'
        return quantity
  
    
    def increase_quantity(self, amount):
        self.quantity += amount
        

    def decrease_quantity(self, amount):
       if self.quantity >= amount:
           self.quantity -= amount
          
       else:
            print('Недостаточное кол-во экземпляров')


