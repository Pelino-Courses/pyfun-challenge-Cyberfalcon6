class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        course.enroll_student(student)
        student.enroll(course)

    def __str__(self):
        return f"Enrollment: {self.student.name} -> {self.course.name}"