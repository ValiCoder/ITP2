while True:
    print("Hello Student! Let's calculate your average grade!")

    print("Please enter your name!")
    name = input()

    print("Okay, " + name + ", please enter your exam scores!")

    while True:
        try:
            Exam1 = int(input("Enter Exam 1 score: "))
            if Exam1 < 0 or Exam1 > 100:
                print("Please enter a number from 0 to 100")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number from 0 to 100")
#while True это цикличный луп который прерывается когда пользователь вводит число 0 до 100
#except ловит ошибку если вводится не int и вместо неё выводит текст говорящий пользователю о том что надо ввести число
    while True:
        try:
            Exam2 = int(input("Enter Exam 2 score: "))
            if Exam2 < 0 or Exam2 > 100:
                print("Please enter a number from 0 to 100")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number from 0 to 100")

    while True:
        try:
            Exam3 = int(input("Enter Exam 3 score: "))
            if Exam3 < 0 or Exam3 > 100:
                print("Please enter a number from 0 to 100")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number from 0 to 100")

    print("Calculating...")

    AverageGrade = (Exam1 + Exam2 + Exam3) / 3

    # Calculating
    # results...
    # Student: Ayan
    # Test
    # Scores: 85, 90, 78
    # Average
    # Score: 84.33
    # Grade: B

    print("Student's name: " + name)
    print("Test Scores " + str(Exam1) + ", " + str(Exam2) + ", "+ str(Exam3))
    print("Average Grade: " + str(AverageGrade))

    if AverageGrade > 90:
        print("Your grade is A")
    elif AverageGrade > 80:
        print("Your grade is B")
    elif AverageGrade > 70:
        print("Your grade is C")
    elif AverageGrade > 60:
        print("Your grade is D")
    else:
        print("Your grade is F")

    print("Would you like to know another student's grade? (Yes/No)")

    Answer = input()

    if Answer.lower() == ("yes"):
#.lower переводит ввод пользователя в lowercase, если бы его не было, мне бы пришлось выписать все вариации слова "Yes"
        print("Next student.")
    elif Answer.lower() == ("no"):
        print("Thank you for using my program!")
        print("Shutting down...")
        break
    else:
        print("Didn't quite understand you. Please answer 'Yes' or 'No'")