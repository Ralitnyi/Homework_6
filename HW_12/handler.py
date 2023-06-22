import classes as cl


def hello(*_):
    return 'How can I help you?'

def create_cont(book: cl.AddressBook, name, phone= None, birthday= None):
    name = cl.Name(name)

    if phone:
        phone = cl.Phone(phone)

    if birthday:
        birthday = cl.Birthday(birthday)

    record = cl.Record(name, phone, birthday)
    book.add_record(record)
    return book[name.value].show_all()


def add(book, name, phone):
    book[name].add_phone(phone)
    return f'phone: {phone} was addet to {name}'

def show_all(book):
    result = ''
    
    for name in book:
        # print(book[i])
        person = f"{book[name].show_all()}\n"
        result += person
    return result.strip() if result else "EMPTY"

def delete_cont(book, name):
    del book[name]
    return f"{name} was deleted"

def remov_phone(book, name, phone):
    res = book[name].remove_phone(phone)
    return res

def change_phone(book, name, phone, new_phone):
    return book[name].change_phone(phone, new_phone)

def add_birthday(book, name, birthday):
    return book[name].add_birthday(birthday)

def search(book, value):
    return book.search(value)

def help(help_file):
    with open(help_file, 'r') as file:
        res = file.read()
        file.seek(0)
        return res

FUNC_LIST = {
    'hello': hello,
    'create': create_cont,
    'add': add,
    'show all': show_all,
    'delete': delete_cont,
    'remove': remov_phone,
    'change': change_phone,
    'birthday': add_birthday,
    'search': search,
    'help': help
}