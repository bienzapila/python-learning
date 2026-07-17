n = int(input())
final = []
for _ in range(n):
    k = int(input())
    ans = []
    for _ in range(k):
        s = input().split()
        if s[1] == '5':
            ans.append(True)
        else:
            ans.append(False)
    if any(ans):
        final.append(True)
    else:
        final.append(False)
if all(final):
    print('YES')
else:
    print('NO')