# Transaction (Транзакция):
# Свойства: дата, тип (выдача/возврат), книга, пользователь.
# Методы: запись транзакции, вывод информации о транзакции

import datetime as datetime

class Transaction:
    def __init__(self, transaction_type, book, user):
        
        
        self.transaction_type = transaction_type
        self.book = book
        self.user = user     
        self.date = datetime.datetime.now()
   
    
    def display_info(self):
        print(f'Дата: {self.date} \nТип(выдача\возврат): {self.transaction_type} \nКнига: {self.book.title} \nПользователь: {self.user.name}')

    
 
    
    



