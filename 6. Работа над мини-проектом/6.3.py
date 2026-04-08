text = "To be, or not to be, that is the question!"
nt = ""
for i in range(len(text)):
    if text[i].isalpha():
        if text[i].upper() == text[i]:
            if ord(text[i]) > 73:
                nt += chr(ord(text[i]) - 9)
            else:
                nt += chr(ord(text[i]) + 17)
        elif text[i].lower() == text[i]:
            if ord(text[i]) > 105:
                nt += chr(ord(text[i]) - 9)
            else:
                nt += chr(ord(text[i]) + 17)
    else:
        nt += text[i]

print(nt)
