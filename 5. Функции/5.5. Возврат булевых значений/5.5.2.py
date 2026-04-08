def is_palindrome(text):
    nt = ""
    for i in range(len(text)):
        if text[i].isalpha():
            nt += text[i]
    nt = nt.lower()
    if nt == nt[::-1]:
        return True
    else:
        return False
