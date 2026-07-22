students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        student = {
            "Name": name,
            "Age": age,
            "Marks": marks
        }

        students.append(student)

    elif choice == "2":
        if len(students) == 0:
            print("No Records Found")
        else:
            for s in students:
                print(s)

    elif choice == "3":
        break

    else:
        print("Invalid Choice")