# Task#8:
# Using range() and a for loop:
# • Print all even numbers between 1 and 50
# • Count how many even numbers are printed

count = 0
for i in range(1, 50):
    if i % 2 ==0:
        print(i)
        count += 1
print("Total even numbers: ", count)
