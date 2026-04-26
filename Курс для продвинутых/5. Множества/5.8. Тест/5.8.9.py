setm = {c for c in input().split()}
setn = {c for c in input().split()}
print(*sorted(setm | setn))
