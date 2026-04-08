a, b = int(input()), int(input())
if a > b:
    for _ in range(a, b-1, -1):
        if _ % 17 == 0 or _ % 10 == 9 or (_ % 3 == 0 and _ % 5 == 0):
            print(_)
elif a < b:
    for _ in range(a, b+1):
        if _ % 17 == 0 or _ % 10 == 9 or (_ % 3 == 0 and _ % 5 == 0):
            print(_)
else:
    if a % 17 == 0 or a % 10 == 9 or (a % 3 == 0 and a % 5 == 0):
        print(a)