from course import Course
from student import Student

class Enrollment:
    """
    Represents Student course relationship

    Args:
        student(Student): A student object to enroll
        course(Course): A course object in which the student will enroll
    """
    def __init__(self, student:Student, course:Course):
        self.student = student
        self.course = course
        course.enroll_student(student)
        student.enroll(course)
    def __str__(self):
        return f"Enrollment: {self.student.name} -> {self.course.name}"