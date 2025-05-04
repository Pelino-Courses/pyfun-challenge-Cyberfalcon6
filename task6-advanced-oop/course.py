class Course:
    def __init__(self, name: str, code: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Course name must be a non-empty string.")
        if not isinstance(code, str) or not code.strip():
            raise ValueError("Course code must be a non-empty string.")
        self.name = name
        self.code = code
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

    def __str__(self):
        return f"Course: {self.name}, Code: {self.code}, Enrolled Students: {[student.name for student in self.students]}"