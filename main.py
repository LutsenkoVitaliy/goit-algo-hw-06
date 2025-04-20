from collections import UserDict
import re

class Field: # Базовий клас для полів запису.
  def __init__(self, value):
    self.value = value
        
  def __str__(self):
    return str(self.value)

class Name(Field): # Клас для зберігання імені контакту. Обов'язкове поле.
  def __init__(self, value):
    # if not value:
    #   raise ValueError('Empty value')
    super().__init__(value)

class Phone(Field):
  def __init__(self, value):
    self.validate(value)
    super().__init__(value)

  @staticmethod
  def validate(value):
    if not re.fullmatch(r'\d{10}', value):
      raise ValueError("No more than 10 cgaracters")


class Record: # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
  def __init__(self, name):
    self.name = Name(name) # Реалізовано зберігання об'єкта Name в атрибуті name.
    self.phones = [] # Реалізовано зберігання списку об'єктів Phone в атрибуті phones.

  def add_phone(self, phone: str):
    self.phones.append(Phone(phone)) # Реалізовано метод для додавання - add_phone .На вхід подається рядок, який містить номер телефона.
    
  def remove_phone(self, phone: str): # Реалізовано метод для видалення - remove_phone. На вхід подається рядок, який містить номер телефона.
    self.phones = [p for p in self.phones if p.value != phone]

  def find_phone(self, phone_find: str): 
    for phone in self.phones:
      if phone.value == phone_find:
        return phone
 
    return None    

  def edit_phone(self, old_phone: str, new_phone: str): # Реалізовано метод для редагування - edit_phone. 
  #На вхід подається два аргумента - рядки,які містять старий номер телефона та новий. 
  #У разі некоректності вхідних даних метод має завершуватись помилкою ValueError.
    old_phone_include = self.find_phone(old_phone)
    if old_phone_include:
      new_phone_include = Phone(new_phone)
      index = self.phones.index(old_phone_include)
      self.phones[index] = new_phone_include
    else:
      raise ValueError(f'Phone {old_phone} not found')

  def __str__(self):
    return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict): 
  def add_record(self, contact):
    self.data[contact.name.value] = contact

  def find(self, name):
    if name in self.data:
      return self.data.get(name)
    return None

  def delete(self, name):
    # if name in self.data
    self.data.pop(name)

  # Реалізовано магічний метод __str__ для красивого виводу об’єкту класу AddressBook .


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record('John')
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record) # Contact name: John, phones: 1234567890; 5555555555

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john) # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
print(book)
