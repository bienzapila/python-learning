ans = {}


def show_top_categories(spendings, num):
    for s in spendings:
        if s[0] not in ans:
            ans[s[0]] = s[1]
        elif s[0] in ans:
            ans[s[0]] += s[1]
    final = sorted(ans.values(), reverse=True)[:num]
    a = []
    for s in final:
        for key in ans.keys():
            if ans[key] == s:
                a.append(key)
                break
    a.sort()
    print(*a, sep="\n")
