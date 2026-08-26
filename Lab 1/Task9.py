# Task#9:
# Write a program using a while loop that:
# • Takes a number from the user
# • Prints its multiplication table
# • Stops when the multiplier reaches 10

num = int(input("Enter a number: "))
count = 1
while (count < 10):
    mul = num*count
    print(num," x ", count, " = ", mul)
    count += 1
