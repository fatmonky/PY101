def get_grade(grade1, grade2, grade3):
    mean_grade = (grade1 + grade2 + grade3) // 3
    if mean_grade >= 90 and mean_grade <= 100:
        return "A"
    elif mean_grade >= 80 and mean_grade < 90:
        return "B"
    elif mean_grade >= 70 and mean_grade < 80:
        return "C"
    elif mean_grade >= 60 and mean_grade < 70:
        return "D"
    else:
        return "F"

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True

# model answer:

def get_grade(grade1, grade2, grade3):
    average = (grade1 + grade2 + grade3) / 3

    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'
