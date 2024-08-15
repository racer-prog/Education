grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
journal_dict = {}
sort_students = sorted(students)
for student in sort_students:
    balls = grades[sort_students.index(student)]
    summa = 0
    for ball in balls:
        summa += ball

    journal_dict[student] = summa/len(balls)
    #print(student, journal_dict[student])
print(journal_dict)

