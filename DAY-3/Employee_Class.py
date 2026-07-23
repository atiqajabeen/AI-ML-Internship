class Employee:
    def __init__(self, name,hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked=hours_worked
    def calculate_salary(self):
        return self.hourly_rate*self.hours_worked

name=input("Enter name of Employee: ")
rate=float(input("Enter hourly rate: "))
hours=float(input("Enter Hours worked: "))

emp = Employee(name, rate , hours)
print("Monthly Salary:",emp.calculate_salary())