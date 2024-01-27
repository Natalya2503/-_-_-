# Задача 
# Разработайте систему классов для управления рестораном.
#  Создайте базовый класс "Блюдо" с общими характеристиками (например, название, цена). Затем создайте подклассы для различных типов блюд, таких как "Завтрак" и "Ужин", добавляя специфичные свойства и методы. Реализуйте метод для расчета общей стоимости заказа.

from abc import ABC, abstractmethod
class Dish(ABC):
    def __init__(self, name, price, order_price):
        self.name = name
        self.price = price
        self.order_price = order_price
       
        
    
    @staticmethod
    def validate_price(price):
        if not((type(price) in [int, float]) and price < 0):
            raise 'Цена меньше 0 или не int и не float'
   
    @abstractmethod
    def view_menu(self):
       pass

class Breakfast(Dish):
    def __init__(self, name, price, drink, price_drink, order_price):
        super().__init__( name, price, order_price)
        self.drink = drink
        self.price_drink = price_drink
        self.order_price = self.price + self.price_drink

    @staticmethod
    def validate_price_drink(price_drink):
        if not((type(price_drink) in [int, float]) and price_drink < 0):
                raise 'Цена меньше 0 или не int и не float'
        
    def view_menu(self):
        super().view_menu()
        print(f'Название блюда: {self.name} \nЦена: {self.price} \nНапиток: {self.drink} \nЦена напитка: {self.price_drink} \nСумма заказа: {self.order_price}')
   
class Dinner(Dish):
    def __init__(self, name, price, dessert, price_dessert, order_price):
        super().__init__( name, price, order_price)
        self.dessert = dessert
        self.price_dessert = price_dessert
        self.order_price = self.price + self.price_dessert

    @staticmethod
    def validate_price_dessert(price_dessert):
        if not((type(price_dessert) in [int, float]) and price_dessert < 0):
                raise 'Цена меньше 0 или не int и не float'
        
    def view_menu(self):
        super().view_menu()
        print(f'Название блюда: {self.name} \nЦена: {self.price} \nДесерт: {self.dessert} \nЦена десерта: {self.price_dessert} \nСумма заказа: {self.order_price}')
 
class Price:
    def __init__(self):
        self.dishes = []
    def add_price(self, order):
        self.dishes.append(order)
    def calculate_total_cost(self):
        total_cost = 0
        for dish in self.dishes:
            total_cost += dish.order_price
        return total_cost
        
        
print('Завтрак')
breakfast = Breakfast('Омлет', 100, 'Кофе', 50, '')
breakfast.view_menu()
print('--------------------')
print('Ужин')
dinner = Dinner('Рыба на пару', 250, 'Йогурт', 150, '')
dinner.view_menu()
print('--------------------')
cost = Price()
cost.add_price(breakfast)
cost.add_price(dinner)
total_cost = cost.calculate_total_cost()
print(f'Общая сумма: {total_cost}')







    