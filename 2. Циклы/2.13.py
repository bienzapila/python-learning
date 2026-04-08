#​ a + 3×b + 2×c = m
n, m = int(input()), int(input())
count = 0
for a in range (1, n):
    for b in range (1, n):
        for c in range (1, n):
            if a + 3 * b + 2 * c == m:
                print(a, '+ 3×'+ str(b), '+ 2×'+ str(c), '=', m)
                count += 1
if count == 0:
    print('При заданных n и m решений не существует.') 
