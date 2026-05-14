import decimal as D

d = D.Decimal(input())
a = list((d.as_tuple())[1])
if str(d)[0] == "0":
    a.append(0)
if str(d)[0] == "-" and str(d)[1] == "0":
    a.append(0)
print(max(a) + min(a))
