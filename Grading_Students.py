def gradingStudents(grades):
    # Write your code here
    for i in range(grades_count):
        diff = 5-(grades[i]%5)
        if grades[i] < 38 :
            None
        elif grades[i] % 5 != 0 and diff < 3:
            grades[i] += diff
    return grades