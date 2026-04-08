s = input().split()

for i in range(len(s)):
    k = s[i][0]
    s[i] = s[i][1:] + k + "ки"

print(*s)
