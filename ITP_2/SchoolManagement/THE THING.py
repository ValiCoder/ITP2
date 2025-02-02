from random import choice, randint


from students_grade import *

class Person:
    id_counter = 101

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self._id = Person.id_counter
        Person.id_counter += 1

    def __str__(self):
        return f"ID: {self._id}, Name: {self.__name}, Age: {self.__age}"

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def id(self):
        return self._id


class Student(Person):
    def __init__(self, name, age, test1, test2, test3):
        super().__init__(name, age)
        self.__test1 = test1
        self.__test2 = test2
        self.__test3 = test3
        self.__grade = self.calculate_grade()

    def calculate_grade(self):
        average = calculate_average(self.__test1, self.__test2, self.__test3)
        return convert_to_letter_grade(average)

    def get_details(self):
        return f"{super().__str__()}, Grade: {self.__grade}"

    @property
    def grade(self):
        return self.__grade


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.__subject = subject

    def get_details(self):
        return f"{super().__str__()}, Subject: {self.__subject}"

    @property
    def subject(self):
        return self.__subject


class Student(Person):
    def __init__(self, name, age, test1, test2, test3):
        super().__init__(name, age)
        self.__test1 = test1
        self.__test2 = test2
        self.__test3 = test3
        self.__grade = self.calculate_grade()

    def calculate_grade(self):
        average = calculate_average(self.__test1, self.__test2, self.__test3)
        return convert_to_letter_grade(average)

    def get_details(self):
        return f"{super().__str__()}, Grade: {self.__grade}"

    @property
    def grade(self):
        return self.__grade


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.__subject = subject

    def get_details(self):
        return f"{super().__str__()}, Subject: {self.__subject}"

    @property
    def subject(self):
        return self.__subject


class Classroom:
    def __init__(self, roomNumber):
        self.__roomNumber = roomNumber
        self.__students = []
        self.__teacher = None

    @property
    def roomNumber(self):
        return self.__roomNumber

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
        teacherInfo = f"Teacher: {self.__teacher.name}, Subject: {self.__teacher.subject}" if self.__teacher else "No teacher assigned"
        studentsInfo = "\n".join([f"{i+1}. {student.name} (ID: {student.id}, Grade: {student.grade})" for i, student in enumerate(self.__students)])
        return f"Classroom {self.__roomNumber}:\n{teacherInfo}\nStudents:\n{studentsInfo if studentsInfo else 'No students enrolled'}"


def searchStudentsByGrade(classroom, grade):
    return [student for student in classroom.getStudentList() if student.grade == grade]


def getValidInput(prompt, inputType):
    while True:
        try:
            value = inputType(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid value.")


def getStudentAge(prompt):
    while True:
        age = getValidInput(prompt, int)
        if 7 <= age <= 20:
            return age
        print("Student age must be between 7 and 20. Please try again.")


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


FIRST_NAMES = [
    "Adam", "Adrian", "Aiden", "Alan", "Alex", "Amir", "Andre", "Anthony", "Arthur", "Asher",
    "Benjamin", "Blake", "Caleb", "Cameron", "Carlos", "Carter", "Charlie", "Christian", "Christopher", "Cole",
    "Daniel", "David", "Dean", "Dominic", "Dylan", "Elijah", "Elliot", "Eric", "Ethan", "Evan",
    "Felix", "Finn", "Francis", "Gabriel", "Gavin", "George", "Grayson", "Henry", "Hudson", "Hunter",
    "Ian", "Isaac", "Jack", "Jacob", "James", "Jason", "Jasper", "Jayden", "Jeremy", "Joel",
    "John", "Jonathan", "Jordan", "Joseph", "Julian", "Kevin", "Kyle", "Landon", "Leo", "Liam",
    "Logan", "Louis", "Lucas", "Luke", "Mason", "Matthew", "Max", "Michael", "Miles", "Nathan",
    "Nicholas", "Noah", "Nolan", "Oliver", "Oscar", "Owen", "Patrick", "Paul", "Peter", "Philip",
    "Preston", "Raymond", "Richard", "Robert", "Ryan", "Samuel", "Scott", "Sean", "Sebastian", "Simon",
    "Spencer", "Stephen", "Theodore", "Thomas", "Timothy", "Travis", "Tristan", "Tyler", "Victor", "William"
]

SURNAMES = [
    "Anderson", "Armstrong", "Baker", "Barnes", "Bell", "Bennett", "Black", "Boone", "Bowman", "Bradley",
    "Brooks", "Brown", "Bryant", "Butler", "Campbell", "Carter", "Chambers", "Clark", "Coleman", "Collins",
    "Cook", "Cooper", "Cox", "Crawford", "Davis", "Dixon", "Douglas", "Edwards", "Evans", "Ferguson",
    "Fisher", "Fleming", "Ford", "Foster", "Garcia", "Gibson", "Gonzalez", "Graham", "Grant", "Gray",
    "Green", "Griffin", "Hall", "Hamilton", "Harris", "Harrison", "Hawkins", "Hayes", "Henderson", "Hernandez",
    "Hill", "Hoffman", "Hughes", "Hunter", "Jackson", "James", "Jenkins", "Johnson", "Jones", "Jordan",
    "Keller", "Kelly", "Kennedy", "King", "Knight", "Lambert", "Lawrence", "Lee", "Lewis", "Long",
    "Marshall", "Martin", "Martinez", "Mason", "Matthews", "McCarthy", "McDonald", "Miller", "Mitchell", "Montgomery",
    "Moore", "Morgan", "Morris", "Murphy", "Nelson", "Newman", "Nichols", "Nixon", "Parker", "Patterson",
    "Perez", "Perry", "Phillips", "Porter", "Powell", "Price", "Reed", "Reyes", "Richardson", "Robinson"
]

def generate_random_name():
    first_name = choice(FIRST_NAMES)
    surname = choice(SURNAMES)
    return f"{first_name} {surname}"


def generate_random_score():
    return randint(40, 100)


def createDefaultStudents():
    students = []
    for _ in range(50):
        name = generate_random_name()
        age = randint(7, 19)
        test1 = generate_random_score()
        test2 = generate_random_score()
        test3 = generate_random_score()
        student = Student(name, age, test1, test2, test3)
        students.append(student)
    return students


def createDefaultTeachers():
    teachers = [
        Teacher(generate_random_name(), randint(20, 70), "Chemistry"),
        Teacher(generate_random_name(), randint(20, 70), "Math"),
        Teacher(generate_random_name(), randint(20, 70), "Economics"),
        Teacher(generate_random_name(), randint(20, 70), "Physics"),
        Teacher(generate_random_name(), randint(20, 70), "History")
    ]
    return teachers


def createDefaultClassroom():
    return [Classroom(200), Classroom(201), Classroom(202), Classroom(203), Classroom(204)]


def assignStudentsToClassrooms(students, classrooms):
    for student in students:
        classroom = choice(classrooms)
        classroom.addStudent(student)


def assignTeachersToClassrooms(teachers, classrooms):
    for i, classroom in enumerate(classrooms):
        if i < len(teachers):
            classroom.setTeacher(teachers[i])
        else:
            print(f"No teacher available for classroom {classroom.roomNumber}.")


def displayStudents(students):
    if not students:
        print("No students available.")
    else:
        print("\nList of Students:")
        for student in students:
            print(f"- {student.name} (ID: {student.id}, Age: {student.age}, Grade: {student.grade})")


def displayTeachers(teachers):
    if not teachers:
        print("No teachers available.")
    else:
        print("\nList of Teachers:")
        for teacher in teachers:
            print(f"- {teacher.name} (ID: {teacher.id}, Age: {teacher.age}, Subject: {teacher.subject})")


def main():
    classrooms = createDefaultClassroom()
    students = createDefaultStudents()
    teachers = createDefaultTeachers()

    assignStudentsToClassrooms(students, classrooms)
    assignTeachersToClassrooms(teachers, classrooms)

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
        print("9. Display All Teachers")
        print("10. Exit")

        choice = getValidInput("\nEnter your choice: ", int)

        if choice == 1:
            name = input("Enter student name: ").strip()
            while not name:
                print("Name cannot be empty. Please try again.")
                name = input("Enter student name: ").strip()

            age = getStudentAge("Enter age: ")

            test1 = getTestScore("Enter Test 1 score: ")
            test2 = getTestScore("Enter Test 2 score: ")
            test3 = getTestScore("Enter Test 3 score: ")

            student = Student(name, age, test1, test2, test3)
            students.append(student)
            print(f'Student "{student.name}" added with ID {student.id} and Grade {student.grade}.')


        elif choice == 2:
            name = input("Enter teacher name: ").strip()
            while not name:
                print("Name cannot be empty. Please try again.")
                name = input("Enter teacher name: ").strip()

            age = getTeacherAge("Enter age: ")

            subject = input("Enter subject: ").strip()
            while not subject:
                print("Subject cannot be empty. Please try again.")
                subject = input("Enter subject: ").strip()

            teacher = Teacher(name, age, subject)
            teachers.append(teacher)
            print(f'Teacher "{teacher.name}" added with ID {teacher.id} and Subject "{teacher.subject}".')

        elif choice == 3:
            roomNumber = getValidInput("Enter classroom number: ", int)
            classroom = Classroom(roomNumber)
            classrooms.append(classroom)
            print(f"Classroom {roomNumber} was successfully created!")

        elif choice == 4:
            roomNumber = getValidInput("Enter classroom number: ", int)
            teacherId = getValidInput("Enter teacher ID to assign: ", int)

            classroom = next((c for c in classrooms if c.roomNumber == roomNumber), None)
            teacher = next((t for t in teachers if t.id == teacherId), None)

            if classroom and teacher:
                classroom.setTeacher(teacher)
                print(f'Teacher "{teacher.name}" assigned to classroom {roomNumber} successfully!')
            else:
                print("Classroom or Teacher not found.")

        elif choice == 5:
            roomNumber = getValidInput("Enter classroom number: ", int)
            studentId = getValidInput("Enter student ID: ", int)

            classroom = next((c for c in classrooms if c.roomNumber == roomNumber), None)
            student = next((s for s in students if s.id == studentId), None)

            if classroom and student:
                classroom.addStudent(student)
                print(f'Student "{student.name}" added to classroom {roomNumber} successfully!')
            else:
                print("Classroom or Student not found.")

        elif choice == 6:
            roomNumber = getValidInput("Enter classroom number: ", int)
            classroom = next((c for c in classrooms if c.roomNumber == roomNumber), None)

            if classroom:
                print(classroom)
            else:
                print("Classroom not found.")

        elif choice == 7:
            roomNumber = getValidInput("Enter classroom number: ", int)
            grade = input("Enter grade to search for: ").strip().upper()
            while not grade:
                print("Grade cannot be empty. Please try again.")
                grade = input("Enter grade to search for: ").strip().upper()

            classroom = next((c for c in classrooms if c.roomNumber == roomNumber), None)
            if classroom:
                studentsWithGrade = searchStudentsByGrade(classroom, grade)
                if studentsWithGrade:
                    print(f"Students with grade {grade} in classroom {roomNumber}:")
                    for i, student in enumerate(studentsWithGrade):
                        print(f"{i+1}. {student.name} (ID: {student.id})")
                else:
                    print(f"No students found with grade {grade} in classroom {roomNumber}.")
            else:
                print("Classroom not found.")

        elif choice == 8:
            displayStudents(students)

        elif choice == 9:
            displayTeachers(teachers)

        elif choice == 10:
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

        doNext = input("\nDo you want to continue? (yes/no): ").strip().lower()
        while True:
            if doNext == "yes":
                print("Continuing with the operation...\n")
                break
            elif doNext == "no":
                print("Exiting the School Management System. Thank you!")
                return
            else:
                print("Sorry, didn't understand you, please enter 'yes' or 'no'")
                doNext = input("\nDo you want to continue? (yes/no): ").strip().lower()


if __name__ == "__main__":
    main()