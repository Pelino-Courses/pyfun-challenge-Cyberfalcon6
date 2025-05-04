from student import Student
from instructor import Instructor

class TeachingAssistant(Student, Instructor):
    def __init__(self, name: str, age: int, student_id: str, employee_id: str):
        Student.__init__(self, name, age, student_id)
        Instructor.__init__(self, name, age, employee_id)

    def __str__(self):
        return f"{Student.__str__(self)}, {Instructor.__str__(self)}"