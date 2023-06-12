from collections import UserDict

class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data.update({record.name.value : record})


class Field():
    
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass 


class Phone(Field):
    pass

class Record():
    
    def __init__(self, name, phone= None):
        self.name = name
        if phone:
           self.phones = []
           self.phones.append(phone)

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except AttributeError:
            self.phones = []
            self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for old_phone in self.phones:
            if phone == old_phone.value:
                self.phones.remove(old_phone)

    def change_phone(self, phone, new_phone):
        for old_phone in self.phones:
            if phone == old_phone.value:
                self.phones[self.phones.index(old_phone)] = Phone(new_phone)


if __name__ == "__main__":
    name = Name('Bill')
    # phone = Phone('1234567890')
    rec = Record(name)
    rec.add_phone('1234567890')
    ab = AddressBook()
    ab.add_record(rec)
    print(ab)

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')

