# Task#6:
# University Staff System (Inheritance):
# Create a base class Staff with:
# • Attributes: name, staff_id, department
# • Method: display_info()
# Create subclasses:
# • Teacher (courses, salary)
# • AdminStaff (role, working_hours)
# • ResearchAssistant (research_topic, stipend)
# Override display_info() where needed.

class Staff:
    def __init__(self, name, staff_id, department):
        self.name = name
        self.staff_id = staff_id
        self.department = department
        
    def display_info(self):
        print("Name: ", self.name)
        print("Staff ID: ", self.staff_id)
        print("Department: ", self.department)

class Teacher(Staff):
    def __init__(self, name, staff_id, department, courses, salary):
        super().__init__(name, staff_id, department)
        self.courses = courses
        self.salary = salary

    def display_info(self):
        super().display_info()
        print("Courses: ", self.courses)
        print("Salary: ", self.salary)
        
class AdminStaff(Staff):
    def __init__(self, name, staff_id, department, role, working_hours):
        super().__init__(name, staff_id, department)
        self.role = role
        self.working_hours = working_hours
        
    def display_info(self):
        super().display_info()
        print("Role: ", self.role)
        print("Working Hours: ", self.working_hours)

class ResearchAssistant(Staff):
    def __init__(self, name, staff_id, department, research_topic, stipend):
        super().__init__(name, staff_id, department)
        self.research_topic = research_topic
        self.stipend = stipend

    def display_info(self):
        super().display_info()
        print("Research Topic: ", self.research_topic)
        print("Stipend: ", self.stipend)

teacher = Teacher("Ali", 101, "Computer Science", ["AI", "ML"], 75000)
admin = AdminStaff("Hammad", 201, "Administration", "Office Manager", 20)
ra = ResearchAssistant("Ahsan", 301, "Physics", "Quantum Computing", 2000)


print("Teacher Info:")
teacher.display_info()

print("Admin Staff Info:")
admin.display_info()

print("Research Assistant Info:")
ra.display_info()
