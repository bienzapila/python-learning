text = "Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd."
nt = ""
for i in range(len(text)):
    if text[i].isalpha():
        if text[i].upper() == text[i]:
            if ord(text[i]) < 90:
                nt += chr(ord(text[i]) + 1)
            else:
                nt += chr(ord(text[i]) - 25)
        elif text[i].lower() == text[i]:
            if ord(text[i]) < 122:
                nt += chr(ord(text[i]) + 1)
            else:
                nt += chr(ord(text[i]) - 25)
    else:
        nt += text[i]

print(nt)
