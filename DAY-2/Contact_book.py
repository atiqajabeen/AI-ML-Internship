contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View Contacts")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        number = input("Enter Number: ")
        contacts[name] = number

    elif choice == "2":
        name = input("Enter Name: ")
        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Contact Not Found")

    elif choice == "3":
        name = input("Enter Name: ")
        if name in contacts:
            contacts[name] = input("Enter New Number: ")
            print("Updated Successfully")
        else:
            print("Contact Not Found")

    elif choice == "4":
        name = input("Enter Name: ")
        if name in contacts:
            del contacts[name]
            print("Deleted Successfully")
        else:
            print("Contact Not Found")

    elif choice == "5":
        print(contacts)

    elif choice == "6":
        break

    else:
        print("Invalid Choice")