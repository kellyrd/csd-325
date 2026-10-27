import json

def load_students(student):
    for student in student:
        print(
            f"First Name: {student['F_Name']}   ", 
            f"Last Name: {student['L_Name']}    ", 
            f"Student ID: {student['Student_ID']}   ", 
            f"Email: {student['Email']}"
            )

        # Load the student data from a JSON file
with open("student.json", "r") as file:
    student_data = json.load(file)

# Print original student list
print("     Original Student List:")
print("------------------------------------")
load_students(student_data)

