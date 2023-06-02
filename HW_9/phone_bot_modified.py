

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input."
        except IndexError:
            return "Invalid command."
    return inner


@input_error
def add_contact(name, phone):
    
    with open('phone_book.txt', 'r+') as file:

        contacts = file.readlines()
        if contacts:
            
            if name in " ".join(contacts):
                return f"{name} is already used"
            
            file.write(f"{name} {phone}\n")
            return f"Contact {name}: {phone} added successfully."

        else:
            file.write(f'{name} {phone}\n')
            return f"Contact {name} {phone} added successfully."
        
    

@input_error
def change_contact(name, phone):
    with open('phone_book.txt', 'r') as raw_file:
        lines = raw_file.readlines()
        if name not in ' '.join(lines):
            return f"{name} is not found"

        with open('phone_book.txt', 'w') as output:
            for line in lines:

                
                if line.startswith(name):
                    lines = list(map(lambda x: x.replace(line, f'{name} {phone}\n'), lines))
                    output.writelines(lines)
                    return "Contact updated successfully."
                

@input_error
def get_phone(name):

    with open('phone_book.txt', 'r') as file:

        contacts = file.readlines()
        for cont in contacts:
            if name in cont:
                return cont.removesuffix('\n')
        return f"{name} is not found"
        

def show_all_contacts():
    
    with open('phone_book.txt', 'r') as file:
        return file.read().removesuffix("\n") if file else 'phonebook is empty'

@input_error
def process_command(command):
    command = command.casefold().strip()
    if command == "hello":
        return "How can I help you?"
    
    if command.startswith("add"):
        _, name, phone = command.split(" ")
        return add_contact(name, phone)
    
    if command.startswith("change"):
        _, name, phone = command.split(" ")
        return change_contact(name, phone)
    
    if command.startswith("phone"):
        _, name = command.split(" ")
        return get_phone(name)
    
    if command == "show all":
        return show_all_contacts()
    
    if command in ["good bye", "close", "exit"]:
        return "Good bye!"
    
    return "Invalid command."

def main():
    while True:
        command = input("Enter a command: ")
        result = process_command(command)
        print(result)
        if result == "Good bye!":
            break

if __name__ == "__main__":
    main()