student_ids = ["X142", "B065", "X144"]
student_names = ["Nikita Karpov", "Anna Chernova", "Ruslan Magarov"]
student_grades = [88, 85, 62]

final = [
    {student_ids[i]: {student_names[i]: student_grades[i]}}
    for i in range(len(student_ids))
]
print(final)
