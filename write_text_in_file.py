# Assigning file name
filename = "mylife.txt"

# Open file to append
with open(filename,"a") as file:

    # Loop for multiple entries
    while True:

        # Input from the user
        line = input("Enter line: ")

        # Write newline
        file.write(line + "\n")

        # Ask the user if there are more lines
        more_lines =input("Are there more lines y/n? ").strip().lower()

    # User response if there are more lines
    if more_lines != "y":
        # if use opt not to enter more lines, exit the loop
# Print the output
