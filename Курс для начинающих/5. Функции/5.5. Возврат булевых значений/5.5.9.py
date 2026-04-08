def is_valid_password(password):
    s = password.split(":")
    a = s[0]
    b = s[1]
    c = s[2]

    if a != a[::-1]:
        return False

    cnt = 0
    for i in range(2, int(b)):
        if int(b) % i == 0:
            cnt += 1
    if cnt != 0 or b == "1":
        return False

    if int(c) % 2 != 0:
        return False

    if len(s) > 3:
        return False

    return True
