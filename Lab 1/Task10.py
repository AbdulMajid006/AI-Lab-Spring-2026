# Task#10:
# Create a function that:
# • Accepts variable-length arguments
# • Returns the maximum number
# Create another function that:
# • Accepts keyword arguments
# • Prints them in key : value format

def findmax(*args):
    return max(args)

def printkeyvalues(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

maxnumber = findmax(9, 50, 66, 86, 71)
print("Maximum number:", maxnumber)

printkeyvalues(name="Abdul Majid", age=20, department="Computer Science")
