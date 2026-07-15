mixed_list = ['abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot']

ans = sorted(mixed_list, key=lambda x: ord(str(x)[0]))

ans1 = []
for i in range(len(ans)):
    if type(ans[i]) == int:
        ans1.append(ans[i])
    else:
        point = i
        ans2 = ans[i:]
        break

final = list(sorted(ans1)) + list(sorted(ans2))
print(*final)