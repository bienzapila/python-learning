dict1 = {"apple": 7, "orange": 2, "peach": 5}
dict2 = {"kiwi": 1, "apple": 6, "orange": 2}
for key in dict1.keys():
    if key in dict2:
        dict2[key] += dict1[key]
    else:
        dict2[key] = dict1[key]

print(dict2)
