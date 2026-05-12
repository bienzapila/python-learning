def get_secret_friend(students):
    import random as rnd

    final = {}
    check = list(students).copy()
    flag = False
    while not flag:
        rnd.shuffle(check)
        for i in range(len(students)):
            if students[i] == check[i]:
                break
        else:
            flag = True

    for i in range(len(students)):
        final[students[i]] = check[i]
    return final


students = ("Светлана", "Аркадий", "Борис")
print(get_secret_friend(students))
