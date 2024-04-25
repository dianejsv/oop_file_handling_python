# Initialize list of filename
input_integers = "integers.txt"
result_even_numbers = "double.txt"
result_odd_numbers = "triple.txt"

# Read integers from the file
with open("integers.txt", "r") as file:
    numbers = file.read().split()
    
# Separate even and odd numbers
# Calculate the square of even numbers and the cube of odd numbers
# Write the results
# Closing statement
