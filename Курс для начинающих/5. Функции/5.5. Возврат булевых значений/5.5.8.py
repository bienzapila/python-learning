def is_correct_bracket(text):
    cnt = 0
    for i in range(len(text)):
        if text[i] == "(":
            cnt += 1
        elif text[i] == ")":
            cnt -= 1
        if cnt < 0:
            return False
    if cnt < 0:
        return False
    else:
        return True
