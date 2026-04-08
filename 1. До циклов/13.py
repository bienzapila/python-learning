a, b, c = input(), input(), input()
if (len(a)+len(c))/2==len(b) or (len(a)+len(b))/2==len(c) or (len(b)+len(c))/2==len(a):
    print('YES')
else:
    print('NO')