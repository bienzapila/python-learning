s1, s2 = input(), input()

ans1, ans2 = [], []
for s in s1:
    if s.isalpha():
        ans1.append(s.lower())
for s in s2:
    if s.isalpha():
        ans2.append(s.lower())
ans1.sort(), ans2.sort()

if ans1 == ans2:
    print("YES")
else:
    print("NO")
