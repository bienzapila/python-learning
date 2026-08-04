with open(input()) as file:
    lines = file.readlines()
    ans = []
    for i in range(-1, -len(lines) - 1, -1):
        if i != -len(lines):
            if 'def' in lines[i]:
                if '#' not in lines[i-1]:
                    ans.append(lines[i])
        if i == -len(lines):
            if 'def' in lines[i]:
                ans.append(lines[i])

ans = list(map(lambda x: x[4:], ans[::-1]))
for i in range(len(ans)):
    ind = ans[i].find('(')
    ans[i] = ans[i][:ind]


print(*ans, sep='\n') if len(ans) != 0 else print('Best Programming Team')