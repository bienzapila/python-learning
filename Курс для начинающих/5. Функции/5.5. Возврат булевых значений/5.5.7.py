def is_password_good(password):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(len(password)):
        if password[i].isalpha() and password[i] == password[i].lower():
            cnt1 += 1
        if password[i].isalpha() and password[i] == password[i].upper():
            cnt2 += 1
        if password[i].isdigit():
            cnt3 += 1

    if len(password) >= 8 and cnt1 >= 1 and cnt2 >= 1 and cnt3 >= 1:
        return True
    else:
        return False


