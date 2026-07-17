pw = input()

ans = []

if len(pw) >= 7:
    ans.append(False)
else:
    ans.append(True)

for s in pw:
    if s.isdigit():
        ans.append(False)
        break
else:
    ans.append(True)

for s in pw:
    if s.isalpha() and s == s.capitalize():
        ans.append(False)
        break
else:
    ans.append(True)

for s in pw:
    if s.isalpha() and s != s.capitalize():
        ans.append(False)
        break
else:
    ans.append(True)

if any(ans):
    print('NO')
else:
    print('YES')