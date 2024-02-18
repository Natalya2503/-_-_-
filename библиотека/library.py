




from transaction import Transaction


class Library:
    
    def __init__(self):
        self.books = []
        self.users = []
    

    def add_book(self, book):
        self.books.append(book)
        print(f'Книга "{book.title}" добавлена в библиотеку')
            
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'Книга "{book.title}" удалена из библиотеки')
        else:
            print('Книга не найдена')
         
    def user_register(self, user):
          self.users.append(user)
          print(f'Пользователь {user.name} зарегистрирован')
          
    
    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f'{user.name} удалён')
        else:
            print('Пользователь не найден')
    
    def lend_book(self, book, user):
        if book in self.books:
           if book.quantity > 0:
              book.decrease_quantity(1)
              user.borrowed_books.append(book)
              transaction = Transaction('выдача', book, user)
              transaction.display_info()
              print(f'Книга "{book.title}" взята на прочтение {user.name}')
           else: 
              print('Нет доступных экземпляров')
        else:
            print('Такой книги нет в библиотеке')
    
    def return_book(self, book, user):
        if book in user.borrowed_books:
            book.increase_quantity(1)
            user.borrowed_books.remove(book)
            transaction = Transaction('возврат', book, user)
            transaction.display_info()
            print(f'Книга "{book.title}" возвращена {user.name}')
        else:
            print('В списке пользователя такой книги нет')
    def show_books(self): 
        print('Список книг в библиотеке:')
        for book in self.books:
            if book.quantity > 0:
                print('Название: ', book.title)
                print('Автор: ', book.author)
                print('Жанр: ', book.genre)
                print('Год издания: ', book.year)
                print('Количество экземпляров: ', book.quantity)
                
    def show_users(self):
        print('Список пользователей:')
        for user in self.users:
            print('Имя: ', user.name)
            print('ID: ', user.user_id)
           

   
 
        

   
    
  
             
       
    
    
    
        





    
