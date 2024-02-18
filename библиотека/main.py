from book import Book
from user import User
from library import Library


book1 = Book('Гроза', 'А.Островский', 1982, 'драма', 5)
book2 = Book('Преступление и наказание', 'Ф.Достоевский', 1866, 'роман', 3)
book3 = Book('Война и мир', 'Л.Толстой', 1965, 'роман-эпопея', 10)

library = Library()
library.add_book(book1)
library.add_book(book2)


user1 = User('Валерий Орлов', 345)
user2 = User('Дмитрий Медведев', 675)
user3 = User('Пётр Алексеев', 444)
library.user_register(user1)
library.user_register(user2)

print('Welcome!')
while True:
    command = input('''
Библиотека - 1
Пользователь - 2
Выход - 3
Выберите команду: ''')
    match command:
        case '3':
          print('Good by!')
          break
        case '1':
            while True:
                command = input('''
Список книг в библиотеке  - 1
Добавить книгу в библиотеку - 2
Удалить книгу из библиотеки - 3
Выход - 0
Выберите команду: ''')
                match command:
                    case '0':
                        break
                    case '1':
                        library.show_books()
                    case '2':
                        library.add_book(book3)
                    case '3':
                        library.remove_book(book2)

        case '2':
            while True:
                command = input('''
Список пользователей - 1
Регистрация пользователя - 2 
Информация о пользователе - 3
Удалить пользователя - 4
Выдача книги пользователю - 5
Возврат книги пользователем - 6
Выход - 0
Выберите команду: ''')
                match command:
                 case '0':
                      break
                 case '1':
                        library.show_users()
                        
                 case '2':
                        library.user_register(user3)
                                                
                 case '3':
                        user1.display_info()
                        user2.display_info()
                        user3.display_info()
                 case '4':
                        library.remove_user(user3)
                        
                 case '5':
                        user1.borrow_book(book1, library)
                        user2.borrow_book(book2, library)
                      
                 case '6':
                       user1.return_book(book1, library)
                       user2.return_book(book2, library) 
 

                
                   
                        
                    
                       


                        