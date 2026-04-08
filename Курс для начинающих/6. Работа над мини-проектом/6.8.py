n = int(input())
s = int(input())
sp = ""


while n > 0:
    left = n % s
    n = n // s
    sp += " " + str(left)[::-1]

print(sp[::-1])
