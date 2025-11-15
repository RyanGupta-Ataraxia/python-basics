def student_grade_calculator(s1, s2, s3, s4, s5):
    total = s1 + s2 + s3 + s4 + s5
    percentage = (total / 500) * 100

    if percentage >= 90:
        grade = 'A'
    elif percentage >= 75:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    elif percentage >= 40:
        grade = 'D'
    else:
        grade = 'F'

    return (
        f"This student scored {total} marks, "
        f"with a percentage of {percentage:.2f}%, "
        f"and acquired grade {grade}."
    )
