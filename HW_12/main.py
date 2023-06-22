import handler 
import classes as cl
import pickle

def input_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            
            return func(*args, **kwargs)
        
        except KeyError as key_error:
            print(f"incorrect command: {key_error}")
            main(filename, help_file)

        except TypeError as type_error:
            print(f"correct command but incorrect value: {type_error}")
            main(filename, help_file)

        except ValueError as value_error:
            print(f'incorect birthday. (DD.MM.YYYY) {value_error}')
            main(filename, help_file)

    return wrapper

def parser(string: str) -> tuple:
    string = string.strip().casefold()
    words_list = string.split(' ')

    if words_list[0] in ['good', 'show']:
        command = ' '.join(words_list[:2]).lower()
        arguments = words_list[2:]

    else:
        command = words_list[0].lower()
        arguments = words_list[1:]
    
    return command, arguments

@input_error_handler
def main(filename, help_file):
    
    print("""You can write <help> for info""")

    with open(filename, 'r') as file:
        if not file.read():
            
            with open(filename, 'wb') as fh:
                book = cl.AddressBook()
                pickle.dump(book, fh)
    
    with open(filename, 'rb') as file:
        address_book: cl.AddressBook = pickle.load(file)


    while True:
        
        string = input('Enter: ')
        command, value = parser(string)

        if command in ['close', 'good bye', 'exit']:  
            with open(filename, 'wb') as file:
                pickle.dump(address_book, file)
                
            print('Good bye')  
            break
        
        if command == 'help':
            print(handler.FUNC_LIST[command](help_file))
        
        else:

            result = handler.FUNC_LIST[command](address_book, *value)
            print(result)

            

if __name__ == '__main__':
    filename = 'phone_book.bin'
    help_file = 'help_file.txt'
    main(filename, help_file)