a = input()
if a[:len(a)//2] == (a[-len(a)//2+1:])[::-1]:
    print('YES')
elif a[:len(a)//2] == (a[-len(a)//2:])[::-1]:
    print('YES')
else:
    print('NO')