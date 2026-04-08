# Русский алфавит в верхнем регистре без Ё в кодах символов с 1040 ('А') по 1071 ('Я'), в нижнем регистре - с 1072 ('а') по 1103 ('я')
text = "Блажен, кто верует, тепло ему на свете!"
nt = ""
for i in range(len(text)):
    if text[i].isalpha():
        if text[i].upper() == text[i]:
            if ord(text[i]) > 1061:
                nt += chr(ord(text[i]) - 14)
            else:
                nt += chr(ord(text[i]) + 17)
        elif text[i].lower() == text[i]:
            if ord(text[i]) > 1093:
                nt += chr(ord(text[i]) - 14)
            else:
                nt += chr(ord(text[i]) + 17)
    else:
        nt += text[i]

print(nt)
