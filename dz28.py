# Дописать метод удаления и/или частичного поиска
# контакта (см. текст задания из классной работы)
# Задание из классной работы:
# Написать программу для управления списком
# контактов.
# В качестве примера, добавьте в программу два объекта
# Contact в список контактов
# Так же необходимо выполнить операции по удалению
# контакта и поиску контакта в списке (удаление и поиск
# осуществляется пользователем)
# Результаты операций должны выводятся на экран.


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone_number = phone
    def display_info(self):
        print(f'Имя: {self.name} \nНомер телефона: {self.phone_number}')
class BusinessContact(Contact):
    def __init__(self, name, phone, company):
        super().__init__(name, phone)
        self.company = company

    def display_info(self):
        super().display_info()
        print(f'Компания: {self.company}')
class PhoneBook:
    def __init__(self):
        self.contacts = []
    def add_contact(self, contact):
        self.contacts.append(contact)
    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None
    def remove_contact(self, contact):
        self.contacts.remove(contact)
    def display_contacts(self):
        for contact in self.contacts:
            contact.display_info()



phone_book = PhoneBook()

contact1 = Contact('Иванов Иван', '8-928-722-36-24')
business_contact = BusinessContact('Петров Василий', '8-928-456-34-78', 'Рога и копыта')

phone_book.add_contact(contact1)
phone_book.add_contact(business_contact)

print('Список всех контактов:')
phone_book.display_contacts()


search_contact = input('Введите имя контакта для поиска по телефонной книге: ')
found_contact = phone_book.find_contact(search_contact)

if found_contact:
    print('Найден контакт:')
    found_contact.display_info()
else:
    print(f'Контакт с именем "{search_contact}" не найден')
print('--------------------')

print('Новый список:')
phone_book.remove_contact(contact1)
phone_book.display_contacts()