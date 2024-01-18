# Создать класс "Person" с атрибутами "name", "age", "email" и методами для чтения и записи данных всех трех атрибутов,
# а также реализовать валидацию для атрибута "age":
# должно быть положительным целым числом

class Person:
    def __init__(self, name, age: int, email):
        self.__name = name 
        self.__age = self.validate_age(age)
        self.__email = email
    @staticmethod
    def validate_age(age):
        if type(age) != int:
            raise 'age must be int'
        if age <= 0:
            raise 'age must not be less than zero'
        return age
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = self.validate_age(age)
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email

person = Person('Наталья', 25, 'tetova2503@gmail.com')
person.name = 'Наталья' 
print(person.name)
person.email = 'tetova2503@gmail.com'
print(person.email)
print(person.get_age())        