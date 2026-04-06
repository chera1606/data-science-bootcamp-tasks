# Python Foundations Assignment
# Task: Check if a number is prime

# ask the user to enter a number
num = int(input("Enter a number: "))

# assume the number is prime
is_prime = True

# check if number is less than 2
if num < 2:
    is_prime = False
else:
    # check divisibility from 2 up to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

# print result
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")