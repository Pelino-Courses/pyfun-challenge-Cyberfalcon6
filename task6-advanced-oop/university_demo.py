from student import Student
from instructor import Instructor
from random import randint
from course import Course
from enrollment import Enrollment
from teaching_assistant import TeachingAssistant

class University():

    def __init__(self):
        self.students:list[Student] = [Student("Japhet Niyogakiza", 23, "224002651")]
        self.courses:list[Course] = [Course("Mathematics", "101")]
        self.instructors:list[Instructor] = [Instructor("Karamage J.Claude", 24, str(randint(10000, 99999)))]
        self.enrollments:list[Enrollment] = []
        self.tas:list[TeachingAssistant] = []
        print("Welcome to University Management System")
        print("==========================================")
        print("""
                1. View University Elements 
                2. View Students
                3. View Courses
                4. View Instructors
                5. View Teaching assistants
                6. Add student
                7. Add course
                8. Add Instructor
                9. View enrollments
                10. Enroll a student
                11. Assign Course
                0. Exit
            >>>>| """, end="")
        choice = int(input())
        while choice!=0:
            if choice==1:
                print("""
                    In university management System there are \n
                    - Students
                    - Instructors
                    - Courses 
                    - Teaching Assistants
                    """)
            elif choice==2:
                for student in self.students:
                    print(student)
            elif choice == 3:
                for course in self.courses:
                    print(course)
            elif choice == 4:
                for instructor in self.instructors:
                    print(instructor)
            elif choice == 5:
                for ta in self.tas:
                    print(ta)
            elif choice == 6:
                student_name = input("Student Name: ")
                student_age = int(input("Student age: "))
                student_id = str(randint(10000, 99999))
                temp_student = Student(student_name, student_age, student_id=student_id)
                self.students.append(temp_student)
            elif choice == 7:
                course_name = input("Course Name: ")
                course_code = input("Course code: ")
                temp_course = Course(course_name, course_code)
                self.courses.append(temp_course)
            elif choice == 8:
                instructor_name = input('Instructor Name: ')
                instructor_age = int(input("Instructor age: "))
                instructor_id = str(randint(10000, 99999))
                temp_instructor = Instructor(instructor_name, instructor_age, instructor_id)
                self.instructors.append(temp_instructor)
            elif choice == 9:
                for enrollment in self.enrollments:
                    print(enrollment)
            elif choice == 10:
                for student in self.students:
                    print(student)
                student_id = input("Student ID you want to enroll: ")
                student = self.getStudentById(student_id)
                for course in self.courses:
                    print(course)
                course_id = input("Course ID of Enrollment: ")
                course = self.getCourseById(course_id)
                temp_enrollment = Enrollment(student, course)
                self.enrollments.append(temp_enrollment)
            elif choice == 11:
                for instructor in self.instructors:
                    print(instructor)
                instructor_id = input("Enter instructor id: ")
                instructor = self.getInstructorById(instructor_id)
                for course in self.courses:
                    print(course)
                course_id = input("Enter the course id to assign: ")
                course = self.getCourseById(course_id)
                instructor.assign_course(course)
            else:
                print("Please enter choice between 1 and 5")
            print("""
                1. View University Elements 
                2. View Students
                3. View Courses
                4. View Instructors
                5. View Teaching assistants
                6. Add student
                7. Add course
                8. Add Instructor
                9. View enrollments
                10. Enroll a student
                11. Assign Course
                0. Exit
            >>>>| """, end="")
            choice = int(input())

        # student1 = Student("Alice", 20, "S001")
        # student2 = Student("Rumaga", 22, "S002")
        # instructor = Instructor("Dr. Smith", 45, "E001")
        # course1 = Course("Math 101", "M101")
        # course2 = Course("Physics 101", "P101")

        # Enrollment(student1, course1)
        # Enrollment(student2, course2)

        # instructor.assign_course(course1)
        # instructor.assign_course(course2)

        # ta = TeachingAssistant("Kalisa", 25, "S003", "E002")
        # ta.enroll(course1)
        # ta.assign_course(course2)

        # print(student1)
        # print(student2)
        # print(instructor)
        # print(course1)
        # print(course2)
        # print(ta)
    def getStudentById(self, student_id):
        """
        Returns Student object matching the id passed to it
        """
        for student in self.students:
            if student_id == student.student_id:
                return student
        return None
    def getInstructorById(self, instructor_id):
        """
        Returns Instructor object matching the id passed to it
        """
        for instructor in self.instructors:
            if instructor_id == instructor.instructor_id:
                return instructor
        return None
    def getCourseById(self, course_code):
        """
        Returns Course object matching the id passed to it
        """
        for course in self.courses:
            if course_code == course.code:
                return course
        return None
if __name__ == "__main__":
    Uni = University()
