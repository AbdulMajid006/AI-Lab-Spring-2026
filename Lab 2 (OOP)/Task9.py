# Task#9:
# Employee Payroll System (Protected Members):
# Create an Employee class with protected attributes _name and _salary.
# Create a subclass Manager that accesses and displays these protected members.

class Employee:
    def __init__(self, name, salary):
        self._name = name      
        self._salary = salary   

class Manager(Employee):
    def display_info(self):
        print("Manager Name:", self._name)
        print("Manager Salary:", self._salary)

emp1 = Employee("Abdul Majid", 80000)
mgr1 = Manager("Kamran", 220000)
mgr1.display_info()
