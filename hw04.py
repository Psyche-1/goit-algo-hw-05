from typing import Callable

def input_error(func: Callable):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
        except KeyError:
            return "User name not found."

    return inner

@input_error
def parse_input(user_input: str):
    """Function parse string to get command and other arguments"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args: list[str], contacts: dict[str, str]):
    """Function add phone to contacts by name"""
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: list[str], contacts: dict[str, str]):
    """Function change phone to contacts by name"""
    name, phone = args
    if name not in contacts:
        return f"{name} not found"
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args: list[str], contacts: dict[str, str]):
    """Function show phone to contacts by name"""
    name = args[0]
    return contacts[name]

def show_all(contacts: dict[str, str]):
    """Function show all contacts formatted"""
    return '\n'.join([f'{contact}: {contacts[contact]}' for contact in contacts])

def main():
    """Function get user input and calls other functions by commands"""
    contacts: dict[str, str] = {}
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
