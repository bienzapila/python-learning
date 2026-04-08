a, b, c = input(), input(), input()
ma = max(len(a), len(b), len(c))
mi = min(len(a), len(b), len(c))
if ma == len(a) and mi == len(b):
    print(b, a, sep='\n')
elif ma == len(b) and mi == len(c):
    print(c, b, sep='\n')
elif ma == len(c) and mi == len(a):
    print(a, c, sep='\n')
elif ma == len(a) and mi == len(c):
    print(c, a, sep='\n')
elif ma == len(b) and mi == len(a):
     print(a, b, sep='\n')
elif ma == len(c) and mi == len(b):
     print(b, c, sep='\n')     