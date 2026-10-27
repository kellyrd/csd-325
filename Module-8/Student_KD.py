import json

def load_students(student):
    for student in student:
        print(
            f"First Name:{student['F_Name']}, Last Name: {student['L_Name']}, Student ID: {student['Student_ID']}, Email: {student['Email']}"
            )

        # Load the student data from a JSON file
with open("student.json", "r") as file:
    student_data = json.load(file)

# Print original student list
print("Original Student List:")
print("--------------------")
load_students(student_data)