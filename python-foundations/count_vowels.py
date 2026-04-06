# Python Foundations Assignment
# Task: Count number of vowels in a string

# ask the user to enter a string
text = input("Enter a string: ")

# define vowels
vowels = "aeiouAEIOU"

# counter for vowels
count = 0

# loop through each character in the string
for char in text:
    if char in vowels:
        count += 1

# print the result
print("Number of vowels:", count)