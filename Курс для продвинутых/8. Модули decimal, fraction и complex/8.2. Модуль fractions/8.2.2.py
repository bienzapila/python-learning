s = "0.21 74.5 12.3 -11.77 48.6542 114.55"
from fractions import Fraction as f

s = s.split()
for i in range(len(s)):
    s[i] = float(s[i])
print(f(str(min(s) + max(s))))
