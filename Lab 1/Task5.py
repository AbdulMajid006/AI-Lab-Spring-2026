# Task#5:
# Take 10 numbers from the user and store them in a list.
# Create a set from that list and display:
# • Original list
# • Set
# • Number of duplicate values removed

list = []
for i in range(10):
    num = int(input("Enter a number: "))
    list.append(num)
print("List: ", list)
set = set(list)

print("The Set is: ", set)

diff = len(list) - len(set)
print("Number of duplicate values removed: ", diff)
