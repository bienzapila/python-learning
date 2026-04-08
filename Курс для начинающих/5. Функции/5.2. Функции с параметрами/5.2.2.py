def print_case_counts(s):
    up = 0
    low = 0
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i] == s[i].upper():
                up += 1
            elif s[i] == s[i].lower():
                low += 1
    print(f"Букв в верхнем регистре: {up}")
    print(f"Букв в нижнем регистре: {low}")
