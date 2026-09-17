class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.strip().title()
        self.last_name = last_name.strip().title()
        self.courses = {}

    def add_course(self, course_number, credits, grade):
        self.courses[course_number] = (credits, grade)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_gpa(self):
        if not self.courses:
            return 0.0

        grade_points = {"A":4, "B":3, "C":2, "D":1, "F":0}
        total_points = 0
        total_credits = 0

        for course, (credits, grade) in self.courses.items():
            total_points += grade_points[grade] * credits
            total_credits += credits

        return round(total_points / total_credits, 2)


def is_valid_course_number(course):
    return course.isalnum() and course[0].isalpha() and course[-1].isdigit()


def is_valid_grade(grade):
    return grade.upper() in ["A", "B", "C", "D", "F"]


def is_valid_credits(credits):
    return credits.isdigit() and 1 <= int(credits) <= 10