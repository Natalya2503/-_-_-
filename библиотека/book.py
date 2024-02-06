# Book (Книга):
# Свойства: название, автор, год издания, жанр, количество экземпляров.
# Методы: вывод информации о книге, уменьшение/увеличение количества экземпляров.

class Book:
    __slots__ = ('__name', '__author', 'year_of_publishing', 'genre', '__quantity')
    def __init__(self, name: str, author: str, year_of_publishing: int , genre: str, quantity: int):
        if type(name) != str:
            raise 'name is not string'
        if type(author) != str:
            raise 'author is not string'
        if type(genre) != str:
            raise 'genre is not string'
        self.__name = name
        self.__author = author
        self.year_of_publishing = self.valid_value(year_of_publishing)
        self.genre = genre
        self.__quantity = self.valid_value_quantity(quantity)
    @staticmethod
    def valid_value(year_of_publishing):
        if type(year_of_publishing) != int:
            raise 'год издания должен быть числом'
        if year_of_publishing < 1445 and year_of_publishing > 3000:
            raise 'год издания указан неверно'
        return year_of_publishing
    @staticmethod
    def valid_value_quantity(quantity):
        if type(quantity) != int:
            raise 'количество должно быть числом '
        if quantity < 0:
            raise 'количество не может быть меньше 0'
        return quantity
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = self.valid_value_quantity(quantity)

    @staticmethod
    def valid_copies(copies):
        if type(copies) != int:
            raise 'кол-во передаваемых экземпляров не int'
        if copies <= 0:
            raise 'кол-во передаваемых экземпляров меньше или равно 0'
        
    def display_info(self):
        print(f'Название: {self.__name} \nАвтор: {self.__author} \nГод издания: {self.year_of_publishing} \nЖанр: {self.genre} \nКол-во экземпляров: {self.__quantity}')
    def add_copies(self, copies):
        self.valid_copies(copies)
        self.__quantity += copies
        print(f'Кол-во экземпляров после добавления: {self.__quantity}')
    def decrease_copies(self, copies):
        self.valid_copies(copies)
        if self.__quantity >= copies:
           self.__quantity -= copies
           print(f'Кол-во экземпляров после уменьшения: {self.__quantity}')
        else:
            print('Недостаточное кол-во экземпляров')

book = Book('Гроза', 'А.Островский', 1982, 'драма', 5)
book.display_info()
book.add_copies(8)
book.decrease_copies(4)      
print('----------------')
# book1 = Book('Война и мир', 'Л.Толстой', 1965, 'роман-эпопея', 10)
# book1.display_info()
# book1.add_copies(3)
# book1.decrease_copies(5)
