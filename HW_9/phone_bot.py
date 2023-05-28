import handler
from handler import phone_book

ERROR = '''ERROR
you can use:
hello
add "name" "phone"
change "name" "phone"
phone "name"
show all 
good bye/exit/close
Try again'''

def input_error(func):
        
    def wrapper():
        
        while True:
            try:
                result = func()
                if result == 'stop':
                    break
                if result == 'wrong phone':
                    print('wrong phone, try again.')
            except IndexError as e:
                
                if isinstance(e, IndexError):
                    
                    print(ERROR)
    
    return wrapper

def sanitize_phone_number(phone):

    phone = phone.strip().removeprefix('+').replace('(', '').replace(')', '')

    if len(phone) in [10, 12] and phone.isdigit():

        if len(phone) == 10:
            phone = f'+38' + phone 
        else:
            phone = f'+' + phone 
        return phone
    return 'stop'


def parser(string):
    corect_str = string.casefold().strip()
    
    command = [j for j in handler.FUNC_LIST if j in corect_str][0]

    if command not in ['add', 'change', 'phone']:
        return (command, )

    name_and_phone = (corect_str[corect_str.index(command) + len(command) :]).split(' ')
    
    name_and_phone = [x for x in name_and_phone if x] 

    if command == 'phone':
        name = name_and_phone[0]
        return command, name
    
    name = name_and_phone[0]
    phone = name_and_phone[1]
    phone = sanitize_phone_number(phone)

    if phone == 'stop':
        return ('stop', )

    return command, name, phone



@input_error
def main():

    # while True:
    string = input('Enter "command" "name" "phone": ')
    parsered_string = parser(string)
    command = parsered_string[0]

    if command == 'stop':
        return 'wrong phone'
    
    if command in ['close', 'good bye', 'exit']:
        print(handler.FUNC_LIST[command]())
        return 'stop'
    
    if command == 'show all':
        if phone_book:
            for i in handler.FUNC_LIST[command]():
                print(f'{i[0]}: {i[1]}')
        else:
            print('phonebook is empty')

    else:

        result = handler.FUNC_LIST[command](parsered_string[1:])
        print(result)



if __name__ == '__main__':
    main()

