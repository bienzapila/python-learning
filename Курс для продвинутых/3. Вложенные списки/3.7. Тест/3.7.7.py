mtrx = [["."] * 8 for _ in range(8)]
let = ["a", "b", "c", "d", "e", "f", "g", "h"]
q = input()
q1 = len(mtrx) - int(q[1])
q2 = let.index(q[0])


mtrx[q1][q2] = "Q"

for j in range(8):
    if mtrx[q1][j] != "Q":
        mtrx[q1][j] = "*"

for i in range(8):
    if mtrx[i][q2] != "Q":
        mtrx[i][q2] = "*"

c = q2
for i in range(q1, 8):
    if 0 <= c < 8:
        if mtrx[i][c] != "Q":
            mtrx[i][c] = "*"
        c += 1
c = q2
for i in range(q1, -1, -1):
    if 0 <= c < 8:
        if mtrx[i][c] != "Q":
            mtrx[i][c] = "*"
        c -= 1

c = q2
for i in range(q1, -1, -1):
    if 0 <= c < 8:
        if mtrx[i][c] != "Q":
            mtrx[i][c] = "*"
        c += 1
c = q2
for i in range(q1, 8):
    if 0 <= c < 8:
        if mtrx[i][c] != "Q":
            mtrx[i][c] = "*"
        c -= 1


for row in mtrx:
    print(*row)
