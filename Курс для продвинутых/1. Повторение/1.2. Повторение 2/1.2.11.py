s = input().split()
s.append("запретил")
s.append("букву")

b = [
    "а",
    "б",
    "в",
    "г",
    "д",
    "е",
    "ж",
    "з",
    "и",
    "й",
    "к",
    "л",
    "м",
    "н",
    "о",
    "п",
    "р",
    "с",
    "т",
    "у",
    "ф",
    "х",
    "ц",
    "ч",
    "ш",
    "щ",
    "ъ",
    "ы",
    "ь",
    "э",
    "ю",
    "я",
]

print(*s, "а")
for l in range(len(b)):
    sa = "".join(s)
    if l != len(b) - 1:
        if b[l] not in sa:
            continue
    so = []
    for k in range(len(s)):
        word = ""
        for i in range(len(s[k])):
            if s[k][i] != b[l]:
                word += s[k][i]
        s[k] = word
        if word != "":
            so.append(word)
    if so == []:
        break
    if l != len(b) - 1:
        print(*so, b[l + 1])
