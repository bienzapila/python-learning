m, n = int(input()), int(input())
setm = {input() for _ in range(m)}
setn = {input() for _ in range(n)}
print(len(setm ^ setn)) if len(setm ^ setn) != 0 else print("NO")
