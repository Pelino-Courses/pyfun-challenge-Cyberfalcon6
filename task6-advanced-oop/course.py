from student import Student
class Course:
    """This class will be used to track information about
    courses """
    def __init__(self, name: str, code: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Course name must be a non-empty string.")
        if not isinstance(code, str) or not code.strip():
            raise ValueError("Course code must be a non-empty string.")
        self.name = name
        self.code = code
        self.current = 0
        self.students = []
    def enroll_student(self, student:Student):
        self.students.append(student)
    def __str__(self):
        return f"Course: {self.name}, Code: {self.code}, Enrolled Students: {[student.name for student in self.students]}"
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < len(self.students):
            return self.students[self.current]
        else:
            raise StopIteration
    def showStudents(self):
        for student in self.students:
            print(student)
s1 = Student("Japhet", 32, "224002651")
c1 = Course("Math", "234")
c1.enroll_student(s1)
c1.showStudents()