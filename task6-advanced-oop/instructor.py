from person import Person

class Instructor(Person):
    def __init__(self, name: str, age: int, instructor_id: str):
        super().__init__(name, age)
        if not isinstance(instructor_id, str) or not instructor_id.strip():
            raise ValueError("Employee ID must be a non-empty string.")
        self.instructor_id = instructor_id
        self.courses_taught = []

    def assign_course(self, course):
        self.courses_taught.append(course)

    def __str__(self):
        return f"{super().__str__()}, Instructor ID: {self.instructor_id}, Courses Taught: {[course.name for course in self.courses_taught]}"