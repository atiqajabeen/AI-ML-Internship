class Student:
    def __init__(self,name,roll_no,department):
        self.name=name
        self.roll_no=roll_no
        self.department=department
    def display(self):
        print("\n Student Information")
        print("Name:",self.name)
        print("Roll-No. ", self.roll_no)
        print("Department: ", self.department)

name=input("Enter student name: ")
roll=input("Enter students Roll No. ")
dept=input("Enter students department: ")
student=Student(name,roll,dept)
student.display()
    