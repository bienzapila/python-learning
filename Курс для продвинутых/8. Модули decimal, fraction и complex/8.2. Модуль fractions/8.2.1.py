numbers = ["3.1415", "-2.8", "4.123", "7.856"]
from fractions import Fraction as f

for n in numbers:
    print(f"{n} = {f(str(n))}")
