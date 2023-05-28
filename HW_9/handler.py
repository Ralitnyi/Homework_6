
phone_book = {}

def fnc_hello(_):
    return 'How can I help you?'

def fnc_add(content):

    if content[0] not in phone_book:

        phone_book.update([content])
        return f'{content[0]}: {content[1]} was added'
    return f'Name {content[0]} already in the phonebook, choose another name'

def fnc_change(content):

    if content[0] in phone_book:

        phone_book.update([content])
        return f'{content[0]}: {content[1]} was changed'
    return f'{content[0]} is not in the phonebook'

def fnc_phone(content):
    
    if content[0] in phone_book:
        return f'{content[0]}: {phone_book[content[0]]}'
    return f'{content[0]} is not in the phonebook'

def fnc_show_all():
    
    if phone_book:
        res = [(name, phone) for name, phone in phone_book.items()]
        return res
    else:
        return 'phonebook is empty'


def fnc_bye():
    return 'Good bye!'


FUNC_LIST = {
    'hello': fnc_hello,
    'add': fnc_add,
    'change': fnc_change,
    'show all': fnc_show_all,
    'phone': fnc_phone,
    'good bye': fnc_bye,
    'close': fnc_bye,
    'exit': fnc_bye
    }