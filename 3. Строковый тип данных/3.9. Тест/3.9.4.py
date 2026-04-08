s = input()
count = 0

for i in range(len(s)):
    if s[i] == 'f':
        count += 1
        if count == 2:
            ans = i

if count >= 2:
    print(ans)
elif count == 1:
    print(-1)
else:
    print(-2) 