d = {1: "AEILNORSTU", 2: "DG", 3: "BCMP", 4: "FHVWY", 5: "K", 8: "JX", 10: "QZ"}
s = input()
ans = 0
for c in s:
    for key in d.keys():
        if c in d[key]:
            ans += key
            break

print(ans)
