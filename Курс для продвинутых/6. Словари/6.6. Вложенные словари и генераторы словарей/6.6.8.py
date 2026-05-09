students = {
    "Сергей": (165, 62),
    "Дима": (178, 61),
    "Катя": (162, 62),
    "Диана": (168, 69),
}
final = {
    c: students[c] for c in students if students[c][0] > 167 and students[c][1] < 75
}
print(final)
