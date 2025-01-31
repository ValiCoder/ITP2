from students_grade import calculate_average, convert_to_letter_grade

next_id = 101

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}"

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age


class Student(Person):
    def __init__(self, name, age, student_id, test1, test2, test3):
        super().__init__(name, age)
        self.__student_id = student_id
        self.__test1 = test1
        self.__test2 = test2
        self.__test3 = test3
        self.__grade = self.calculateGrade()

    def calculateGrade(self):
        self.average = calculate_average(self.__test1, self.__test2, self.__test3)
        return convert_to_letter_grade(self.average)

    def get_details(self):
        return f"{super().__str__()}, Student ID: {self.__student_id}, Grade: {self.__grade}, Average score: {self.average}"

    @property
    def student_id(self):
        return self.__student_id

    @property
    def grade(self):
        return self.__grade


class Teacher(Person):
    def __init__(self, name, age, teacher_id, subject):
        super().__init__(name, age)
        self.__teacher_id = teacher_id
        self.__subject = subject

    def getDetails(self):
        return f"{super().__str__()}, Teacher ID: {self.__teacher_id}, Subject: {self.__subject}"

    @property
    def teacher_id(self):
        return self.__teacher_id

    @property
    def subject(self):
        return self.__subject


class Classroom:
    def __init__(self, room_number):
        self.__room_number = room_number
        self.__students = []
        self.__teacher = None

    @property
    def roomNumber(self):
        return self.__room_number

    def addStudent(self, student):
        if isinstance(student, Student):
            self.__students.append(student)
        else:
            raise TypeError("Invalid student object")

    def getStudentList(self):
        return self.__students

    def setTeacher(self, teacher):
        if isinstance(teacher, Teacher):
            self.__teacher = teacher
        else:
            raise TypeError("Invalid teacher object")

    def getTeacher(self):
        return self.__teacher

    def __str__(self):
        teacher_info = f"Teacher: {self.__teacher.name}, Subject: {self.__teacher.subject}" if self.__teacher else "No teacher assigned"
        students_info = "\n".join(
            [f"{i + 1}. {student.name} (ID: {student.student_id}, Grade: {student.grade})" for i, student in
             enumerate(self.__students)])
        return f"Classroom {self.__room_number}:\n{teacher_info}\nStudents:\n{students_info if students_info else 'No students enrolled'}"


def searchStudentsByGrade(classroom, grade):
    students = classroom.getStudentList()
    return list(filter(lambda student: student.grade == grade, students))


def getNextID():
    global next_id
    current_id = next_id
    next_id += 1
    return current_id


def getValidInput(prompt, input_type):
    while True:
        try:
            value = input_type(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid value.")


def getStudentAge(prompt):
    while True:
        age = getValidInput(prompt, int)
        if 5 <= age <= 20:
            return age
        print("Student age must be between 5 and 20. Please try again.")


def getTeacherAge(prompt):
    while True:
        age = getValidInput(prompt, int)
        if 20 <= age <= 70:
            return age
        print("Teacher age must be between 20 and 70. Please try again.")


def getTestScore(prompt):
    while True:
        score = getValidInput(prompt, float)
        if 0 <= score <= 100:
            return score
        print("Test score must be between 0 and 100. Please try again.")


def createDefaultStudents():
    global next_id
    students = [
        Student("Alice Selezneva", 15, getNextID(), 85, 90, 88),
        Student("Bob Smith", 16, getNextID(), 78, 82, 80),
        Student("Charlie B. Goode", 14, getNextID(), 92, 88, 90),
        Student("Pavel Durov", 17, getNextID(), 75, 80, 78),
        Student("Kamala Harris", 15, getNextID(), 88, 85, 90),
        Student("Fiona Shrek", 16, getNextID(), 95, 92, 94),
        Student("Stasik x_X__2011__X_x", 14, getNextID(), 70, 75, 72),
        Student("Bob Marley", 15, getNextID(), 82, 85, 80),
        Student("Alan Walker", 16, getNextID(), 90, 88, 92),
        Student("Dwayne Johnson", 17, getNextID(), 85, 90, 87)
    ]
    return students


def createDefaultTeachers():
    global next_id
    teachers = [
        Teacher("Walter White", 55, getNextID(), "Chemistry"),
        Teacher("Isaac Newton", 45, getNextID(), "Math"),
        Teacher("Mister Beast", 39, getNextID(), "Economics")
    ]
    return teachers


def createDefaultClassroom():
    classrooms = [
        Classroom(200),
        Classroom(201),
        Classroom(202)
    ]
    return classrooms


def displayStudents(students):
    if not students:
        print("No students available.")
    else:
        print("\nList of Students:")
        for student in students:
            print(f"- {student.name} (ID: {student.student_id}, Age: {student.age}, Grade: {student.grade})")


def displayTeachers(teachers):
    if not teachers:
        print("No teachers available.")
    else:
        print("\nList of Teachers:")
        for teacher in teachers:
            print(f"- {teacher.name} (ID: {teacher.teacher_id}, Age: {teacher.age}, Subject: {teacher.subject})")


def main():
    students = createDefaultStudents()
    teachers = createDefaultTeachers()
    classrooms = createDefaultClassroom()

    while True:
        print("\nSchool Management System Menu:")
        print("1. Add a Student")
        print("2. Add a Teacher")
        print("3. Create a Classroom")
        print("4. Assign Teacher to a Classroom")
        print("5. Add Student to a Classroom")
        print("6. Display Classroom Information")
        print("7. Search for Students by Grade")
        print("8. Display All Students")
        print("9. Exit")

        choice = getValidInput("\nEnter your choice: ", int)

        if choice == 1:
            name = input("Enter student name: ").strip()
            while not name:
                print("Name cannot be empty. Please try again.")
                name = input("Enter student name: ").strip()

            age = getStudentAge("Enter age: ")

            student_id = getNextID()
            print(f"The Automatically Assigned Student ID: {student_id}")

            test1 = getTestScore("Enter Test 1 score: ")
            test2 = getTestScore("Enter Test 2 score: ")
            test3 = getTestScore("Enter Test 3 score: ")

            student = Student(name, age, student_id, test1, test2, test3)
            students.append(student)
            print(f'Student "{name}" added successfully with grade {student.grade}!')

        elif choice == 2:
            name = input("Enter teacher name: ").strip()
            while not name:
                print("Name cannot be empty. Please try again.")
                name = input("Enter teacher name: ").strip()

            age = getTeacherAge("Enter age: ")

            teacher_id = getNextID()
            print(f"The Automatically Assigned Teacher ID: {teacher_id}")

            subject = input("Enter subject: ").strip()
            while not subject:
                print("Subject cannot be empty. Please try again.")
                subject = input("Enter subject: ").strip()

            teacher = Teacher(name, age, teacher_id, subject)
            teachers.append(teacher)
            print(f'Teacher "{name}" added successfully!')

        elif choice == 3:
            room_number = getValidInput("Enter classroom number: ", int)
            classroom = Classroom(room_number)
            classrooms.append(classroom)
            print(f"Classroom {room_number} was successfully created!")

        elif choice == 4:
            room_number = getValidInput("Enter classroom number: ", int)
            teacher_id = getValidInput("Enter teacher ID to assign: ", int)

            classroom = next((c for c in classrooms if c.roomNumber == room_number), None)
            teacher = next((t for t in teachers if t.teacher_id == teacher_id), None)

            if classroom and teacher:
                classroom.setTeacher(teacher)
                print(f'Teacher "{teacher.name}" assigned to classroom {room_number} successfully!')
            else:
                print("Classroom or Teacher not found.")

        elif choice == 5:
            room_number = getValidInput("Enter classroom number: ", int)
            student_id = getValidInput("Enter student ID: ", int)

            classroom = next((c for c in classrooms if c.roomNumber == room_number), None)
            student = next((s for s in students if s.student_id == student_id), None)

            if classroom and student:
                classroom.addStudent(student)
                print(f'Student "{student.name}" added to classroom {room_number} successfully!')
            else:
                print("Classroom or Student not found.")

        elif choice == 6:
            room_number = getValidInput("Enter classroom number: ", int)
            classroom = next((c for c in classrooms if c.roomNumber == room_number), None)

            if classroom:
                print(classroom)
            else:
                print("Classroom not found.")

        elif choice == 7:
            room_number = getValidInput("Enter classroom number: ", int)
            grade = input("Enter grade to search for: ").strip().upper()
            while not grade:
                print("Grade cannot be empty. Please try again.")
                grade = input("Enter grade to search for: ").strip().upper()

            classroom = next((c for c in classrooms if c.roomNumber == room_number), None)
            if classroom:
                students_with_grade = searchStudentsByGrade(classroom, grade)
                if students_with_grade:
                    print(f"Students with grade {grade} in classroom {room_number}:")
                    for i, student in enumerate(students_with_grade):
                        print(f"{i + 1}. {student.name} (ID: {student.student_id})")
                else:
                    print(f"No students found with grade {grade} in classroom {room_number}.")
            else:
                print("Classroom not found.")

        elif choice == 8:
            displayStudents(students)
            displayTeachers(teachers)

        elif choice == 9:
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

        print("\n=======================================================")

        doNext = input("\nDo you want to continue? (yes/no): ").strip().lower()
        while True:
            if doNext == "yes":
                print("Continuing with the operation...\n")
                break
            elif doNext == "no":
                print("Exiting the Library Management System. Thank you!")
                return
            else:
                print("Sorry, didn't understand you, please enter 'yes' or 'no'")
                doNext = input("\nDo you want to continue? (yes/no): ").strip().lower()


if __name__ == "__main__":
    main()