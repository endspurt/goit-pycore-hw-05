# Defining the decorator for handling input errors
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Key error: Please enter a valid name."
        except ValueError:
            return "Value error: Please provide both name and phone or a correct name."
        except IndexError:
            return "Index error: Your input seems incomplete."
    return inner

# Function to add a contact
@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Please provide both name and phone.")
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Function to get a contact's phone number
@input_error
def get_contact(args, contacts):
    if len(args) != 1:
        raise ValueError("Please enter one name.")
    name = args[0]
    return f"{name}: {contacts[name]}"

# Function to list all contacts
def list_all_contacts(contacts):
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

# Main function to run the bot
def main():
    contacts = {}
    while True:
        command = input("Enter a command: ")
        if command == "add":
            args = input("Enter the argument for the command: ").split()
            print(add_contact(args, contacts))
        elif command == "phone":
            args = input("Enter the argument for the command: ").split()
            print(get_contact(args, contacts))
        elif command == "all":
            print(list_all_contacts(contacts))
        elif command == "exit":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()

