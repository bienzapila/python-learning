def replace_homoglyphs(text):
    homoglyphs = {
        "e": "е",
        "y": "у",
        "o": "о",
        "p": "р",
        "a": "а",
        "ʍ": "м",
        "ʙ": "в",
        "Φ": "Ф",
        "k": "к",
        "x": "х",
        "c": "с",
        "E": "Е",
        "T": "Т",
        "ȹ": "ф",
        "Ͷ": "И",
        "ʜ": "н",
        "O": "О",
        "P": "Р",
        "A": "А",
        "H": "Н",
        "K": "К",
        "Ƅ": "ь",
        "ͷ": "и",
        "ɯ": "ш",
        "X": "Х",
        "C": "С",
        "B": "В",
        "M": "М",
        "π": "п",
        "3": "З",
        "Γ": "Г",
        "ʮ": "ч",
    }
    ans = ""
    for s in text:
        for key in homoglyphs.keys():
            if s == key:
                ans += homoglyphs[key]
                break
        else:
            ans += s
    return ans


print(replace_homoglyphs(input()))
