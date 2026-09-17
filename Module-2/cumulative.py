from student import Student, is_valid_course_number, is_valid_grade, is_valid_credits

print("Welcome to the GPA Calculator!\n")

while True:   # OUTER LOOP for multiple students
    first_name = input("Please enter student's first name: ").strip()
    last_name = input("Please enter student's last name: ").strip()

    student = Student(first_name, last_name)

    print("\nYou may enter 'q' at ANY time to exit course entry.\n")

    while True:   # INNER LOOP for course entry
        course_number = input("Please enter course number: ").strip()
        if course_number.lower() == "q":
            break

        if not is_valid_course_number(course_number):
            print("Invalid course number. Must be alphanumeric and start with a letter.\n")
            continue

        grade = input("Enter grade (A, B, C, D, F): ").strip()
        if grade.lower() == "q":
            break

        if not is_valid_grade(grade):
            print("Invalid grade. Must be A, B, C, D, or F.\n")
            continue

        credits = input("Enter number of credits (1-10): ").strip()
        if credits.lower() == "q":
            break

        if not is_valid_credits(credits):
            print("Invalid credits. Must be a number between 1 and 10.\n")
            continue

        # Add course
        student.add_course(course_number.upper(), int(credits), grade.upper())
        print("Course added!\n")

    # SUMMARY OUTPUT
    print("\n----------------------------------------")
    print(f"Student: {student.get_full_name()}")
    print("----------------------------------------")
    print("Course     Credits     Grade")
    print("----------------------------------------")

    for course, (credits, grade) in student.courses.items():
        print(f"{course:<10} {credits:<11} {grade}")

    print("----------------------------------------")
    print(f"GPA: {student.get_gpa()}\n")

    # Ask if user wants another student
    another = input("Add another student? (Press Enter for yes, 'n' for no): ").strip().lower()
    if another == "n":
        print("\nGood Bye!")
        break

print("\nProgram ended.\n")
