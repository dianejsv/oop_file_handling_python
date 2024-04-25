# Initialize list of filename
input_integers = "integers.txt"
result_even_numbers = "double.txt"
result_odd_numbers = "triple.txt"

# Read integers from the file
with open("integers.txt", "r") as file:
    numbers = file.read().split()
# Separate even and odd numbers
even_numbers = [int(num) for num in numbers if int(num) % 2 == 0]
odd_numbers = [int(num) for num in numbers if int(num) % 2 != 0]

# Calculate the square of even numbers and the cube of odd numbers
even_squared = [num ** 2 for num in even_numbers]
odd_cubed = [num ** 3 for num in odd_numbers]

# Write the results
with open(result_even_numbers, 'w') as file:
    for num in even_squared:
        file.write(str(num) + '\n')

with open(result_odd_numbers, 'w') as file:
    for num in odd_cubed:
        file.write(str(num) + '\n')

# Closing statement
