from student import Student
from instructor import Instructor
from course import Course
from enrollment import Enrollment
from teaching_assistant import TeachingAssistant

def main():
    student1 = Student("Alice", 20, "S001")
    student2 = Student("Bob", 22, "S002")
    instructor = Instructor("Dr. Smith", 45, "E001")
    course1 = Course("Math 101", "M101")
    course2 = Course("Physics 101", "P101")

    Enrollment(student1, course1)
    Enrollment(student2, course2)

    instructor.assign_course(course1)
    instructor.assign_course(course2)

    ta = TeachingAssistant("Charlie", 25, "S003", "E002")
    ta.enroll(course1)
    ta.assign_course(course2)

    print(student1)
    print(student2)
    print(instructor)
    print(course1)
    print(course2)
    print(ta)

if __name__ == "__main__":
    main()