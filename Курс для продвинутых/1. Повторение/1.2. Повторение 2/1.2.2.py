s = input().split()
cnt = 0
for i in range(len(s)):
    if i == 0:
        continue
    if int(s[i]) > int(s[i - 1]):
        cnt += 1

print(cnt)
