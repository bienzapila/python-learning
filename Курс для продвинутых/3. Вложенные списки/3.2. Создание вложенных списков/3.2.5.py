s = input().split()
ans = []

for i in range(len(s)):
    if i == 0:
        a = [s[0]]
    elif i == len(s) - 1:
        if s[i] != s[i - 1]:
            ans.append(a)
            ans.append(list(s[i]))
        else:
            a.append(s[i])
            ans.append(a)
    elif s[i] != s[i - 1]:
        ans.append(a)
        a = [s[i]]
    elif s[i] == s[i - 1]:
        a.append(s[i])


print(ans)
