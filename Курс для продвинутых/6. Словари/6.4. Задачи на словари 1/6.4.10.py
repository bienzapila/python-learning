ans1 = {}
ans = {}
for _ in range(int(input())):
    s = input().split(": ")
    ans1[s[0]] = [s[1]]

for _ in range(int(input())):
    s = input().split(": ")
    ans1[s[0]].append(s[1])
    ans[s[0]] = None


for key in ans1.keys():
    for i in range(len(ans1[key])):
        ans1[key][i] = ans1[key][i].split(":")
        for k in range(2):
            ans1[key][i][k] = int(ans1[key][i][k])

for key in ans1.keys():
    if len(ans1[key]) == 2:
        if ans1[key][1][0] < 3:
            ans1[key][1][0] += 24

for key in ans1.keys():
    if len(ans1[key]) == 2:
        if ans1[key][0][1] <= ans1[key][1][1]:
            t = (ans1[key][1][0] - ans1[key][0][0]) * 60
            t += ans1[key][1][1] - ans1[key][0][1]
        else:
            t = ans1[key][1][1] + (60 - ans1[key][0][1])
            t += (ans1[key][1][0] - ans1[key][0][0] - 1) * 60
        ans1[key].append(t)

for key in ans.keys():
    for key1 in ans1.keys():
        if key == key1:
            ans[key] = ans1[key1]


for key in ans.keys():
    if len(ans[key]) == 3:
        if ans[key][2] <= 120:
            print(f"{key}: плата не взимается")
        else:
            print(f"{key}: {(ans[key][2]-120)*3}₽")
