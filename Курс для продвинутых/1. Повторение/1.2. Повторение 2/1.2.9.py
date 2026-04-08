s = input()
cnt = 0
mx = 0

for i in range(len(s)):
    if s[i] != "Р":
        cnt = 0
    elif s[i] == "Р":
        cnt += 1

    if mx < cnt:
        mx = cnt

print(mx)
