students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        marks = input("Enter Marks: ")

        students.append({
            "Name": name,
            "Age": age,
            "Marks": marks
        })

        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No Students Found")
        else:
            for student in students:
                print(student)

    elif choice == "3":
        search = input("Enter Student Name: ")

        found = False

        for student in students:
            if student["Name"].lower() == search.lower():
                print(student)
                found = True

        if not found:
            print("Student Not Found")

    elif choice == "4":
        search = input("Enter Student Name: ")

        found = False

        for student in students:
            if student["Name"].lower() == search.lower():
                student["Age"] = input("Enter New Age: ")
                student["Marks"] = input("Enter New Marks: ")
                print("Record Updated")
                found = True

        if not found:
            print("Student Not Found")

    elif choice == "5":
        search = input("Enter Student Name: ")

        found = False

        for student in students:
            if student["Name"].lower() == search.lower():
                students.remove(student)
                print("Record Deleted")
                found = True
                break

        if not found:
            print("Student Not Found")

    elif choice == "6":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")