# Write a program that:
# • Takes a number from the user
# • Prints whether it is Prime or Not using a loop

num = int(input("Enter a number: "))
if num <= 1:
    print("The number is not prime")
elif num == 2:
    print("The number is prime")
else:
    check = 2
    prime = True

    while check < num:
        if num % check == 0:
            prime = False
            break
        check += 1
    if prime:
        print("The number is prime")
    else:
        print("The number is not prime")
