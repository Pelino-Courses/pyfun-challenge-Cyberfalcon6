from person import Person

class Instructor(Person):
    def __init__(self, name: str, age: int, employee_id: str):
        super().__init__(name, age)
        if not isinstance(employee_id, str) or not employee_id.strip():
            raise ValueError("Employee ID must be a non-empty string.")
        self.employee_id = employee_id
        self.courses_taught = []

    def assign_course(self, course):
        self.courses_taught.append(course)

    def __str__(self):
        return f"{super().__str__()}, Employee ID: {self.employee_id}, Courses Taught: {[course.name for course in self.courses_taught]}"