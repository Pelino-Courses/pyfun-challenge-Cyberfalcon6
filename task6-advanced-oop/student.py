from person import Person

class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Student ID must be a non-empty string.")
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def __str__(self):
        return f"{super().__str__()}, Student ID: {self.student_id}, Enrolled Courses: {[course.name for course in self.courses]}"