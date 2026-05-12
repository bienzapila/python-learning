import decimal as D

d = D.Decimal(input())
a = list((d.as_tuple())[1])
if d[0] == 0:
    a.append(0)
print(max(a) + min(a))
