def calculate_average(test1, test2, test3):
    return (test1 + test2 + test3) / 3


def convert_to_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"