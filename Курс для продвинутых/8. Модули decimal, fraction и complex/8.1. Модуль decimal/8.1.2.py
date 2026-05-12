s = "12.3 1.8 3.6 -1.2 0.5 -14.2 86.5 10.3"
import decimal as d

s = s.split(" ")
for k in range(len(s)):
    s[k] = d.Decimal(s[k])
print(sum(s))
print(*sorted(s, reverse=True)[:5])
