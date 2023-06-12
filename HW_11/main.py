from collections import UserDict
from datetime import date


class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data.update({record.name.value : record})

    def iterator(self, n):
        list_data = list(self.data.items())
        while len(list_data) > n:
            yield list_data[0 : n]
            list_data = list_data[n : ]
        yield list_data
        
class Field():
    
    def __init__(self, value):
        self.__private_value = None
        self.value = value

    @property
    def value(self):
        return self.__private_value
    
    @value.setter
    def value(self, new_value):
        self.__private_value = new_value

    @value.deleter
    def value(self):
        print(f'"{self.__private_value}" was deleted')
        del self.__private_value

class Name(Field):
    pass 

class Phone(Field):
    

    def check_correct(self, phone):
        phone = str(phone).replace(')', '').replace('(', '')

        if phone.isdigit() and len(phone) in [10, 12]:
            return True
        return False
    

    @property
    def value(self):
        return self.__private_value
    
    @value.setter
    def value(self, new_value):

        if self.check_correct(new_value):
            self.__private_value = new_value
            # print(f"New phone: {self.__private_value}")

        else:
            print(f'Incorrect phone')

class Birthday(Field):
    
    def check_correct(self, d):
        return isinstance(d, date)

    @property
    def value(self):
        return self.__private_value
    
    @value.setter
    def value(self, new_value):

        if self.check_correct(new_value):
            self.__private_value = new_value
            # print(f"Birthday: {self.__private_value}")

        else:
            print(f'Incorrect date')

class Record():
    
    def __init__(self, name, phone= None, birthday= None):
        self.name = name

        if phone:
           self.phones = []
           self.phones.append(phone)

        if birthday:
            self.birthday = birthday

    def add_birthday(self, birthday):
        self.birthday = birthday

    def days_to_birthday(self):

        today = date.today()
        try: 
            day_birthday = date(year= today.year, month= self.birthday.value.month, day= self.birthday.value.day)
            return day_birthday - today
        except AttributeError:
            return 'no birthday'

    def add_phone(self, phone):
        try:
            self.phones.append(phone)
        except AttributeError:
            self.phones = []
            self.phones.append(phone)

    def remove_phone(self, phone):
        for old_phone in self.phones:
            if phone == old_phone.value:
                self.phones.remove(old_phone)

    def change_phone(self, phone, new_phone):
        for old_phone in self.phones:
            if phone == old_phone.value:
                self.phones[self.phones.index(old_phone)] = Phone(new_phone)


