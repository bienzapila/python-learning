s = input()
res = ''

for i in range(len(s)):
    if i % 3 == 0:
        continue
    else:
        res += s[i]
print(res)