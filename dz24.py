# Класс SantaClaus
# Атрибуты: имя, возраст, количество подарков.
# Методы: give_gifts(), update_age().
# НЕОБЯЗАТЕЛЬНО: Интерфейс для отправки подарков и обновления возраста.

class SantaClaus:
    def __init__(self, name, age, number_of_gifts):
        self.name = name
        self.age = age
        self.number_of_gifts = number_of_gifts


    def display_info(self):
        print(f'name: {self.name} \nage: {self.age} \nnumber_of_gifts: {self.number_of_gifts}')

    def give_gifts(self, new_number_of_gifts):
       if new_number_of_gifts >= 0:
           self.number_of_gifts = new_number_of_gifts
   
    
    def update_age(self, new_age):
        if new_age >= 0:
            self.age = new_age
       

gifts = SantaClaus('Иван', '10', '2')
gifts.display_info()


print('---------Интерфейс--------')
while True:
    command = input("""
1 - показать информацию
2 - отредактировать количество
3 - отредактировать возраст
4 - выход
""")
    if command == '4':
        print('-----Выход----')
        break
    elif command == '1':
        print('----Показать информацию----')
        gifts.display_info()
    elif command == '3':
        print('----Отредактировать возраст----')
        new_age = int(input('Введите ваш возраст: '))
        gifts.update_age(new_age)
    elif command == '2':
        print('----Отредактировать кол-во подарков----')
        new_number_of_gifts = int(input('Сколько подарков вы хотите: '))
        gifts.give_gifts(new_number_of_gifts)
  
                    
