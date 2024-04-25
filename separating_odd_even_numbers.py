# Welcome message
print("Welcome to this Program!")

# Read the integers from "numbers.txt"
with open("numbers.txt", "r") as file:
    numbers = file.readlines()
 
# Strip any whitespaces
numbers = {int(num.strip()) for num in numbers}

# Separate odd and even integers from the list
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Write even integers to "even.txt"
# Write odd number integers to "odd.txt"
# Print the output
