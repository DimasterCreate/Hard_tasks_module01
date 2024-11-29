grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_score = {}
students_list = list(students)
students_list.sort()

student_score.update({students_list[0]:sum(grades[0])/len(grades[0]), students_list[1]:sum(grades[1])/len(grades[1])})
student_score.update({students_list[2]:sum(grades[2])/len(grades[2]), students_list[3]:sum(grades[3])/len(grades[3])})
student_score.update({students_list[4]:sum(grades[4])/len(grades[4])})

print('Список студентов со средним баллом: ', student_score)
