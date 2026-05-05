def transform(text):
    ans = {}
    for i in range(len(text)):
        if text[i] not in ans:
            ans[text[i]] = set([i])
        else:
            ans[text[i]].add(i)
    return ans
