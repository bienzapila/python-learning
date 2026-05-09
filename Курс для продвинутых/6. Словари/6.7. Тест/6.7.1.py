my_dict = {
    "math_grades": [10, 7, 36, 14, 25],
    "physics_grades": [14, 28, 7, 10, 36, 5],
    "chemistry_grades": [10, 14, 19, 20, 21],
    "geography_grades": [10, 15, 19, 34],
}

final = {}
for key in my_dict.keys():
    a = []
    for i in range(len(my_dict[key])):
        if my_dict[key][i] <= 20:
            a.append(my_dict[key][i])
    final[key] = a


print(final)
