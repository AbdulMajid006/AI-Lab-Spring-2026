# Task#6:
# Create a dictionary to store student details:
# • name
# • marks
# • grade
# Using conditions:
# • Assign grade based on marks
# • Update the dictionary and print it

student = {
    "name": input("Enter student name: "),
    "marks": int(input("Enter marks: "))
}

if student["marks"] >=80:
    student["grade"] = "A+"
elif student["marks"] >=70:
    student["grade"] = "A"
elif student["marks"] >=60:
    student["grade"] = "B"
else:
    student["grade"] = "C"

print("Student Details: ", student)
