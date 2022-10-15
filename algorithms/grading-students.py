def gradingStudents(grades):
    for i in grades:
        if (i % 5) > 2 and i > 37:
            grades[grades.index(i)] += (5 - i%5)
    return grades
