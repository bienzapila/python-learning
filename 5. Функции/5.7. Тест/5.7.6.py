def is_magic(date):
    s = date.split(".")
    return int(s[0]) * int(s[1]) == int(s[2][2:])
