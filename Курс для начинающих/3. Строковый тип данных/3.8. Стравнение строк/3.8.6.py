n = int(input())
s1 = ''
ar1 = 0
count1 = 0
cnt = 0

for i in range(n):
    s = input()
    
    for k in range(len(s)):
        if s[k] == ',':
            count = k
            break
    for l in range(len(s)):
        if s[l] == ' ':
            ar = l
            break

    if s[:ar] > s1[:ar1]:
        s1 = s
        ar1 = ar
        count1 = count
        cnt += 1
        continue
    elif s[:ar] < s1[:ar1]:
        print('NO')
        break
    else:
        if s[count:] > s1 [count1:]:
            s1 = s
            ar1 = ar
            count1 = count
            cnt += 1
            continue
        elif s[count:] < s1 [count1:]:
            print('NO')
            break
    
if cnt == n:
    print('YES')