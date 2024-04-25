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
with open("even.txt", "w") as even_file:
    for num in even_numbers:
        even_file.write(str(num) + "\n")

# Write odd number integers to "odd.txt"
with open("odd.txt", "w") as odd_file:
    for num in odd_numbers:
        odd_file.write(str(num) + "\n")

# Print the output
print("Files 'even.txt' and 'odd.txt' created successfully.")
