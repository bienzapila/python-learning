a = input()
a1 = a[:len(a)//2 + len(a) % 2]
a2 = a[-len(a)//2 + len(a) % 2:]
if len(a) == 1:
    print(a)
else:
    print(a2+a1)