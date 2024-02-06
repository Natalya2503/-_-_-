# Задача 1: Управление банковским счетом
# Реализуйте класс BankAccount, который представляет банковский счет. Класс должен содержать атрибуты balance (баланс) и методы deposit (положить деньги на счет) и withdraw (снять деньги со счета). Создайте собственный класс исключения InsufficientFundsError, который будет возбуждаться при попытке снятия суммы, превышающей текущий баланс.

class InsufficientFundsError(Exception):
    def __str__(self):
        return f'Ошибка: не хватает денег на балансе'
  
class BankAccount:
    __slots__ = ('__name', '__balance')
    def __init__(self, name: str, balance: float = 0):
        if type(name) != str:
            raise 'имя должно быть str'
       
       
        self.__name = name
        self.__balance = self.valid_balance(balance)
    
    
    @staticmethod
    def valid_balance(balance):
        if balance < 0:
            raise 'баланс меньше 0'
        return balance
         
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance):
        self.__balance = self.valid_balance(balance)
    
    @staticmethod
    def valid_money(money):
        if  money < 0:
            raise 'money меньше 0'
        return money
    
    def display_info(self):
        print(f'Имя: {self.__name} \nБаланс: {self.__balance}')
        
    def deposit(self, money):
        self.valid_money(money)
        self.__balance += money
        print(f'{self.__name} положил на счёт {money} \nБаланс: {self.__balance}')

    def withdraw(self, money):
        self.valid_money(money)
        if self.__balance < money:
            raise InsufficientFundsError
        self.__balance -= money
        print(f'{self.__name} снял со счёта {money} \nБаланс: {self.__balance}')

account = BankAccount('Василий Егоров', 1000)
account.display_info()
print('----------------')
account.deposit(2000)
print('----------------')
account.withdraw(1000)