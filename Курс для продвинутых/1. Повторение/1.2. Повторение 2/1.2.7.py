s1, s2 = input(), input()

if s1 == "ножницы":
    if s2 == "камень":
        print("Руслан")
    elif s2 == "бумага":
        print("Тимур")
    else:
        print("ничья")
elif s1 == "камень":
    if s2 == "бумага":
        print("Руслан")
    elif s2 == "ножницы":
        print("Тимур")
    else:
        print("ничья")
elif s1 == "бумага":
    if s2 == "ножницы":
        print("Руслан")
    elif s2 == "камень":
        print("Тимур")
    else:
        print("ничья")
