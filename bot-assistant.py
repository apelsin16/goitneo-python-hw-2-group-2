def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such record exists"
        except IndexError:
            return "Give me name and phone please."
        

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return 'such a record exists.'
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if contacts[args[0]]:
        contacts.update({args[0]: args[1]})
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    return contacts[args[0]]

@input_error
def show_all(contacts):
    contacts_string = ''
    for name, phone in contacts.items():
        contacts_string += f"{name}: {phone}\n"
    if contacts_string:
        return contacts_string
    else:
        return "No contacts"

def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()