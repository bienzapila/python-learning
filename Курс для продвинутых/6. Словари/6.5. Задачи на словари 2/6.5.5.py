def dict_diff(data1, data2):
    ans = {}
    for key1 in data1.keys():
        for key2 in data2.keys():
            if key1 == key2:
                if data1[key1] == data2[key2]:
                    ans[key1] = "unchanged"
                else:
                    ans[key1] = "changed"
        else:
            ans[key1] = "deleted"
    for key2 in data2.keys():
        if key2 not in data1:
            ans[key2] = "added"
    return ans
