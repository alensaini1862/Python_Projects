import json
import os

FILE = "contacts.json"

# Load contacts
def load_contacts():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

# Save contacts
def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)

contacts = load_contacts()

while True:
    print("\n--- Contact Book ---")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        if not contacts:
            print("No contacts found")
        else:
            for name, number in contacts.items():
                print(f"{name} : {number}")

    elif choice == '2':
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        save_contacts(contacts)
        print("Contact saved ✅")

    elif choice == '3':
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"{name} : {contacts[name]}")
        else:
            print("Contact not found ❌")

    elif choice == '4':
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            save_contacts(contacts)
            print("Deleted ✅")
        else:
            print("Contact not found ❌")

    elif choice == '5':
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")