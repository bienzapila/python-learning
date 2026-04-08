text = "Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг."
nt = ""
for i in range(len(text)):
    if text[i].isalpha():
        if text[i].upper() == text[i]:
            if ord(text[i]) < 1047:
                nt += chr(ord(text[i]) + 25)
            else:
                nt += chr(ord(text[i]) - 7)
        elif text[i].lower() == text[i]:
            if ord(text[i]) < 1079:
                nt += chr(ord(text[i]) + 25)
            else:
                nt += chr(ord(text[i]) - 7)
    else:
        nt += text[i]

print(nt)
