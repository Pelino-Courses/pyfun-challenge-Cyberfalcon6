from __future__ import annotations
from typing import TYPE_CHECKING
from person import Person
if TYPE_CHECKING:
    from course import Course
class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Student ID must be a non-empty string.")
        self.student_id = student_id
        self.courses:list[Course] = []
    def enroll(self, course:Course):
        from course import Course
        if not isinstance(course, Course):
            raise TypeError("the parameter should of 'Course' type")
        else:
            self.courses.append(course)

    def __str__(self):
        return f"{super().__str__()}, Student ID: {self.student_id}, Enrolled Courses: {[course.name for course in self.courses]}"