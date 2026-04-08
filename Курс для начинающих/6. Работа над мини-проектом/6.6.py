# A 65 Z 90 a 97 z 122
def caesar_swap(word):
    nt = ""
    cnt = 0
    for w in word:
        if w.isalpha():
            cnt += 1
    n = cnt
    for i in range(len(word)):
        if word[i].isalpha():
            if word[i].upper() == word[i]:
                if ord(word[i]) > 90 - n:
                    nt += chr(ord(word[i]) - (26 - n))
                else:
                    nt += chr(ord(word[i]) + n)
            elif word[i].lower() == word[i]:
                if ord(word[i]) > 122 - n:
                    nt += chr(ord(word[i]) - (26 - n))
                else:
                    nt += chr(ord(word[i]) + n)
        else:
            nt += word[i]
    return nt


s = input().split()
for sp in s:
    print(caesar_swap(sp), end=" ")
