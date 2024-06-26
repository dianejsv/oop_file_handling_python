# Open the file consisting of student names and GWAs
with open("academic_record.txt", "r") as file:
    students_record = file.readlines()

# Initialize variables to store highest GWA along with student's name
highest_gwa = float("inf")
top_student = ""

# Checking of the student with highest GWA
for line in students_record:
    name, gwa = line.strip().split(",")
    gwa = float(gwa)

    if gwa <= highest_gwa:
        highest_gwa = gwa
        top_student = name
# Display student's name with highest GWA
print(f"The student with the highest GWA is {top_student} with a GWA of {highest_gwa}.")

