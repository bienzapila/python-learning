import decimal as D

s = "0.0 5.42 8.63 10.25 1.6 -8.5 -13.0"
s = s.split(" ")
for i in range(len(s)):
    s[i] = D.Decimal(s[i])
print(min(s) + max(s))
