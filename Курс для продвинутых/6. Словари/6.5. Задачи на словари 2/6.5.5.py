def dict_diff(data1, data2):
    ans = {}

    for key in data1.keys():
        if key in data2.keys():
            if data2[key] == data1[key]:
                ans[key] = 'unchanged'
            else:
                ans[key] = 'changed'
        else:
            ans[key] = 'deleted'
    
    for key in data2.keys():
        if key in ans:
            continue
        else:
            ans[key] = 'added'

    return ans


