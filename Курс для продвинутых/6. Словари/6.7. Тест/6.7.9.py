final = {}
n = int(input())
for _ in range(n):
    c = input().split()
    if c[0] not in final:
        final[c[0]] = {c[1]: int(c[2])}
    else:
        if c[1] not in final[c[0]]:
            final[c[0]][c[1]] = int(c[2])
        else:
            final[c[0]][c[1]] += int(c[2])

for key1 in sorted(list(final.keys())):
    print(f"{key1}:")
    for key2 in sorted(list(final[key1].keys())):
        print(f"{key2} {final[key1][key2]}")
