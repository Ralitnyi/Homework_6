from collections import UserDict

class AdressBook(UserDict):
    
    def add_record(self, record):
        self.data.update({record.name.value : record.phones})


class Field():
    
    def __init__(self, value):
        self.value = value

class Name(Field):
    
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    
    def __init__(self, value):
        super().__init__(value)

class Record():
    
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for old_phone in self.phones:
            if phone == old_phone.value:
                self.phones.remove(old_phone)

    def change_phone(self, phone, new_phone):
        for old_phone in self.phones:
            if phone == old_phone.value:
                self.phones[self.phones.index(old_phone)] = Phone(new_phone)


book = AdressBook()
record = Record('Ivan')
record.add_phone('325352432')
record.add_phone('2')
record.remove_phone('2')
record.remove_phone('dfg')
record.change_phone('325352432', '1')
book.add_record(record)

second_record = Record('Igor')
second_record.add_phone('3252423')
second_record.remove_phone('3252423')
book.add_record(second_record)

print(book)


