h1, m1, h2, m2 = int(input()), int(input()), int(input()), int(input())

def fmt_print(h, m):
    if m <= 9 and h <= 9:
        print('0', h, ':', '0', m, sep='')
    elif m <= 9:
        print(h, ':', '0', m, sep='')
    elif h <= 9:
        print('0', h, ':', m, sep='')
    else:
        print(h, ':', m, sep='')

fmt_print(h1, m1)
while h1 != h2 or m1 != m2:
    m1 += 1
    if m1 == 60:
        m1 = 0
        h1 += 1
    fmt_print(h1, m1)

