# Defining the decorator for handling input errors
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Key error: please enter a valid key."
        except ValueError:
            return "Value error: please ensure your input is correct."
        except IndexError:
            return "Index error: your input seems to be short."
    return inner

# Example function using the decorator to handle the add contact functionality
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Other functions can be defined similarly and decorated with @input_error
# For instance, a function to retrieve a contact's phone number
@input_error
def get_contact(args, contacts):
    name = args[0]
    return f"{name}: {contacts[name]}"

# Creating a simple CLI for the bot
def main():
    contacts = {}
    while True:
        command = input("Enter a command: ")
        if command == "add":
            args = input("Enter name and phone: ").split()
            print(add_contact(args, contacts))
        elif command == "phone":
            name = input("Enter name: ").split()
            print(get_contact(name, contacts))
        elif command == "all":
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        elif command == "exit":
            break

if __name__ == "__main__":
    main()
