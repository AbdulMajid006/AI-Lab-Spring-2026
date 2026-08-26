# 1: Student Profile System (Basics of Class & Object)
# Create a Student class with attributes name, roll_no, and program.
# Add a method display_info() to show student details.
# Create at least two student objects and display their information.

class Student:
    def __init__(self, name, roll_no, program):
        self.name = name
        self.roll_no = roll_no
        self.program = program

    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Program: {self.program}")

s1 = Student("Ali", 123, "CS")
s2 = Student("Hammad", 421, "SE")

s1.display_info()
s2.display_info()
