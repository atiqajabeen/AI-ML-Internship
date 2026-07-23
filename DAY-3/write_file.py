while True:
    name=input("Enter name of student: ")
    rollno=input("Enter Roll_No of students: ")
    department=input("Enter department of students: ")
    file=open("students.txt","a")
    file.write(f"{name},{rollno},{department}")
    file.close()
    choice=input("Add another student ? Yes/No: ")
    if choice.lower() != "yes":
        break
print("Records Saved Successfully")