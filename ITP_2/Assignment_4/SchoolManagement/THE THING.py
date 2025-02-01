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
        if 5 <= age <= 19:
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

import random

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

    first_name = random.choice(FIRST_NAMES)
    surname = random.choice(SURNAMES)
    return f"{first_name} {surname}"


def generate_random_score():

    return random.randint(40, 100)


def createDefaultStudents():
    global next_id
    minAge = 7
    maxAge = 19
    num_students = 50

    students = []
    for i in range(num_students):
        name = generate_random_name()
        age = random.randint(minAge, maxAge)
        student_id = getNextID()
        test1 = generate_random_score()
        test2 = generate_random_score()
        test3 = generate_random_score()
        student = Student(name, age, student_id, test1, test2, test3)
        students.append(student)

    return students


def createDefaultTeachers():
    global next_id
    teachers = [
        Teacher(generate_random_name(), random.randint(20, 70), getNextID(), "Chemistry"),
        Teacher(generate_random_name(), random.randint(20, 70), getNextID(), "Math"),
        Teacher(generate_random_name(), random.randint(20, 70), getNextID(), "Economics"),
        Teacher(generate_random_name(), random.randint(20, 70), getNextID(), "Physics"),
        Teacher(generate_random_name(), random.randint(20, 70), getNextID(), "History")
    ]
    return teachers


def createDefaultClassroom():
    classrooms = [
        Classroom(200),
        Classroom(201),
        Classroom(202),
        Classroom(203),
        Classroom(204)
    ]
    return classrooms


def assignStudentsToClassrooms(students, classrooms):

    for student in students:
        classroom = random.choice(classrooms)
        classroom.addStudent(student)


def assignTeachersToClassrooms(teachers, classrooms):

    random.shuffle(teachers)  # Shuffle teachers to randomize assignments
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
        print("8. Display All People")
        print("9. Exit")

        choice = getValidInput("\nEnter your choice: ", int)

        if choice == 1:
            name = generate_random_name()  # Generate a random name
            print(f"Generated Student Name: {name}")

            age = getStudentAge("Enter age: ")

            student_id = getNextID()
            print(f"The Automatically Assigned Student ID: {student_id}")

            test1 = generate_random_score()
            test2 = generate_random_score()
            test3 = generate_random_score()

            student = Student(name, age, student_id, test1, test2, test3)
            students.append(student)

            # Assign the new student to a random classroom
            classroom = random.choice(classrooms)
            classroom.addStudent(student)
            print(f'Student "{name}" added successfully with grade {student.grade} and assigned to classroom {classroom.roomNumber}!')

        elif choice == 2:
            name = generate_random_name()  # Generate a random name
            print(f"Generated Teacher Name: {name}")

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
                # Check if the teacher is already assigned to another classroom
                if any(t.teacher_id == teacher_id for t in [c.getTeacher() for c in classrooms if c.getTeacher()]):
                    print(f'Teacher "{teacher.name}" is already assigned to another classroom.')
                else:
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
                print("Exiting the School Management System. Thank you!")
                return
            else:
                print("Sorry, didn't understand you, please enter 'yes' or 'no'")
                doNext = input("\nDo you want to continue? (yes/no): ").strip().lower()


if __name__ == "__main__":
    main()