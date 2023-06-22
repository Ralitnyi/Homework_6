from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):
    
    def __init__(self):
        super().__init__()

    
    def add_record(self, record):
        self.data.update({record.name.value : record})

    def iterator(self, n):
        list_data = list(self.data.items())
        while len(list_data) > n:
            yield list_data[0 : n]
            list_data = list_data[n : ]
        yield list_data

    def search(self, value):
        name_similarity = []
        phone_similarity = []
        result = ''

        for name in self.data:

            if value in name:
                name_similarity.append(name)
            
            for phone in self.data[name].phones:
                if value in phone.value:
                    phone_similarity.append(name)

        for name in name_similarity:
            result += f'{self.data[name].show_all()}\n'

        for name in phone_similarity:
            result += f'{self.data[name].show_all()}\n'

        return result.strip() if result else 'nothing was found'

        
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
    
    def __repr__(self):
        return self.value

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

        # if self.check_correct(new_value):
        self.__private_value = str(new_value)
            # print(f"New phone: {self.__private_value}")

        # else:
        #     print(f'Incorrect phone')

    def __eq__(self, obj: object) -> bool:
        return self.value == obj.value
    
    def __repr__(self) -> str:
        return self.value

class Birthday(Field):
    
    def check_correct(self, d):
        return isinstance(d, datetime)

    @property
    def value(self):
        return self.__private_value
    
    @value.setter
    def value(self, new_value):

        new_value = datetime.strptime(new_value, '%d.%m.%Y')
        if self.check_correct(new_value):
            self.__private_value = new_value
            # print(f"Birthday: {self.__private_value}")

        else:
            print(f'Incorrect date')
    
    # def __repr__(self):
    #     return self.value

class Record():
    
    def __init__(self, name, phone= None, birthday= None):
        self.name = name
        self.phones = []
        self.birthday = birthday
        
        if phone:
           self.phones.append(phone)


    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        return f'{self.name} has birthday: {self.birthday.value}'

    def days_to_birthday(self):

        today = datetime.today()
        try: 
            day_birthday = datetime(year= today.year, month= self.birthday.value.month, day= self.birthday.value.day)
            return day_birthday - today
        except AttributeError:
            return 'no birthday'

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except AttributeError:
            self.phones = []
            self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone = Phone(phone)
        len_befor_remove = len(self.phones)

        for old_phone in self.phones:
            if phone == old_phone:
                self.phones.remove(old_phone)
        len_after_remove = len(self.phones)

        if len_befor_remove == len_after_remove:
            return f'there no phone: {phone}'
        return f'phone: {phone} was deleted'

    def change_phone(self, phone, new_phone):
        phone = Phone(phone)

        for old_phone in self.phones:
            if phone == old_phone:
                self.phones[self.phones.index(old_phone)] = Phone(new_phone)
        
        if Phone(new_phone) in self.phones:
            return f'phone: {phone} was changed to {new_phone}'
        return f'there no {phone}'

    def show_all(self):
        if self.birthday:
            return f'name: {self.name.value}, phones: {self.phones}, birthday: {self.birthday.value}'

        else:
            return f'name: {self.name.value}, phones {self.phones}'


