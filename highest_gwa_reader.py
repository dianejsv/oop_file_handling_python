# Open the file consisting of student names and GWAs
with open("academic_report.txt", "r") as file:
    students_record = file.readlines()

# Initialize variables to store highest GWA along with student's name
highest_gwa = float("inf")
top_student = ""

# Checking of the student with highest GWA
for line in students_record:
# Display student's name with highest GWA
