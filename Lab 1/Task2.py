# Take a string input from the user.
# Display:
# • First character
# • Middle character
# • Last character
# • Length of the string

string = str(input("Enter a string"))
length = len(string)

first = string[0]
middle = string[(length-1)//2]
last = string[length-1]

print("First character: ", first)
print("First character: ", middle)
print("First character: ", last)
