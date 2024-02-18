# User (Пользователь):
# Свойства: имя, ID, список взятых книг.
# Методы: вывод информации о пользователе, взятие/возврат книги




class User:
    
    def __init__(self, name: str, user_id: int):
        if type(name) != str:
            raise 'name is not string'
        if type(user_id) != int:
            raise 'ID must be int'
       
       
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
    def display_info(self):
         print(f'Имя: {self.name} \nID: {self.user_id} \nВзятые книги: ')
         if len(self.borrowed_books) > 0:
             for book in self.borrowed_books:
               print(f'{book.title} - {book.author}')
         else:
             print('У пользователя нет взятых книг')
  
    def borrow_book(self, book, library):
        library.lend_book(book, self)
        
    def return_book(self, book, library):
        library.return_book(book, self)
       












