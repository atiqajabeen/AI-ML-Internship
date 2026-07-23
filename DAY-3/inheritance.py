class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Name: ",self.name)
class Student(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
    def display(self):
        super().display()
        print("Roll No. ",self.roll)
class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject
    def display(self):
        super().display()
        print("Subject: ",self.subject)
student=Student("Atiqa","22AI001")
teacher=Teacher("XYZ","Artificial Intelligence")
print("Student")
student.display
print("Teacher")
teacher.display


        