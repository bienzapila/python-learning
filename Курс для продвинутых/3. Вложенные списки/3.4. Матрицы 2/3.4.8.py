mtrx = []
for _ in range(8):
    mtrx.append(["."] * 8)

let = ["a", "b", "c", "d", "e", "f", "g", "h"]
xy = input()
for k in range(len(let)):
    if xy[0] == let[k]:
        y = k
x = 8 - (int(xy[1]))

mtrx[x][y] = "N"
for i in range(len(mtrx)):
    for j in range(len(mtrx[0])):
        if (
            i == x + 2
            and j == y + 1
            or i == x + 1
            and j == y + 2
            or i == x - 2
            and j == y - 1
            or i == x - 1
            and j == y - 2
            or i == x + 2
            and j == y - 1
            or i == x + 1
            and j == y - 2
            or i == x - 2
            and j == y + 1
            or i == x - 1
            and j == y + 2
        ):
            mtrx[i][j] = "*"


for row in mtrx:
    print(*row)
