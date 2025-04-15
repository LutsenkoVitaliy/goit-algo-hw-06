from collections import UserDict

class Field: # Базовий клас для полів запису.
  def __init__(self, value):
    self.value = value
        
  def __str__(self):
    return str(self.value)

class Name(Field): # Клас для зберігання імені контакту. Обов'язкове поле.
    pass

class Phone(Field): # Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр).
  #Наслідує клас Field. Значення зберігaється в полі value .
	pass

class Record: # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
  def __init__(self, name):
    self.name = Name(name) # Реалізовано зберігання об'єкта Name в атрибуті name.
    self.phones = [] # Реалізовано зберігання списку об'єктів Phone в атрибуті phones.

  def add_phone(self, phone: str):
    self.phones.append(Phone(phone)) # Реалізовано метод для додавання - add_phone .На вхід подається рядок, який містить номер телефона.
    
  def remove_phone(self, phone: str): # Реалізовано метод для видалення - remove_phone. На вхід подається рядок, який містить номер телефона.
    self.phones = [p for p in self.phones if p.value != phone]    

  def edit_phone(self, old_phone: str, new_phone: str): # Реалізовано метод для редагування - edit_phone. 
  #На вхід подається два аргумента - рядки,які містять старий номер телефона та новий. 
  #У разі некоректності вхідних даних метод має завершуватись помилкою ValueError.
    pass
  
  def find_phone(self, phone: str): # Реалізовано метод для пошуку об'єктів Phone - find_phone. 
  #На вхід подається рядок, який містить номер телефона. Метод має повертати або об’єкт Phone, або None .
    pass

  def __str__(self):
    return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict): #Клас для зберігання та управління записами.
  # Реалізовано метод add_record, який додає запис до self.data. Записи Record у AddressBook зберігаються як значення у словнику. 
  # В якості ключів використовується значення Record.name.value.
  def add_record(self, contact: Record):
    self.data[contact.name.value] = contact

  # Реалізовано метод find, який знаходить запис за ім'ям. 
  # На вхід отримує один аргумент - рядок, якій містить ім’я. Повертає об’єкт Record, або None, якщо запис не знайден.  
  def find(self, name):
    print(self.data.get(name))  

  # Реалізовано метод delete, який видаляє запис за ім'ям.
  def delete(self, name):
    self.data.pop(name)
  # Реалізовано магічний метод __str__ для красивого виводу об’єкту класу AddressBook .


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# # Видалення запису Jane
# book.delete("Jane")
