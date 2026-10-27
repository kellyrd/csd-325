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
print("\n     Original Student List:")
print("------------------------------------")
load_students(student_data)

# Create a new student
new_student = {
    "F_Name": "Kelly",
    "L_Name": "Dimick",
    "Student_ID": "123456",
    "Email": "kdimick@my365.bellevue.edu"
}

# Add the new student to the list
student_data.append(new_student)

# Print updated student list
print("\n     Updated Student List:")
print("------------------------------------")
load_students(student_data)

# Save the updated student list back to the JSON file
with open("student.json", "w") as file:
    json.dump(student_data, file, indent=4)

print("\n     .json file was updated.")
