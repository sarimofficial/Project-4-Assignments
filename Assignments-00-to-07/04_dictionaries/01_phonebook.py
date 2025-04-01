# Initialize an empty phonebook dictionary
phonebook = {}

def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter phone number: ")
    phonebook[name] = number
    print(f"Added {name} to phonebook.")

def lookup_contact():
    name = input("Who are you looking for? ")
    if name in phonebook:
        print(f"{name}'s number is {phonebook[name]}")
    else:
        print(f"{name} not found in phonebook.")

def display_all():
    print("\nPhonebook Contacts:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Deleted {name} from phonebook.")
    else:
        print(f"{name} not found in phonebook.")

# Main program loop
while True:
    print("\nPhonebook Options:")
    print("1. Add contact")
    print("2. Lookup contact")
    print("3. Display all contacts")
    print("4. Delete contact")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        lookup_contact()
    elif choice == "3":
        display_all()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")