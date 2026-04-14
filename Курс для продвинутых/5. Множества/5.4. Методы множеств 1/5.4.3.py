s = input().lower().split()
for k in range(len(s)):
    spa = ""
    for i in range(len(s[k])):
        if s[k][i].isalpha():
            spa += s[k][i]
    s[k] = spa
print(len(set(s)))
