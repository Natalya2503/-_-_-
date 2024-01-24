# Задача 
# Создайте класс Book, представляющий книгу. Реализуйте магические методы сравнения (==, !=, <, >, <=, >=) на основе сравнения года издания книги. Книги сравниваются по году издания

class Book:
    def __init__(self, name, year_of_publishing: int):
        self.name = name
        self.year_of_publishing = year_of_publishing
    
    def __eq__(self, other):
        return self.year_of_publishing == other.year_of_publishing
    def __ne__(self, other):
        return self.year_of_publishing != other.year_of_publishing 
    def __gt__(self, other):
        return self.year_of_publishing > other.year_of_publishing
    def __lt__(self, other):
        return self.year_of_publishing < other.year_of_publishing
    def __ge__(self, other):
        return self.year_of_publishing >= other.year_of_publishing
    def __le__(self, other):
        return self.year_of_publishing <= other.year_of_publishing

book1 = Book('Война и мир', 1873)
book2 = Book('Мастер и Маргарита', 1966)
book_name = book1.name
book_name1 = book2.name
print(book1 == book2)
print(book1 != book2)
print(f'Книга {book_name1} моложе книги {book_name}. ')
print(f'Книга {book_name} старее книги {book_name1}.')
print(book1 <= book2)
print(book2 >= book1)