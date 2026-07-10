def greet(name, *args):
    ans = [*name] if name in (list, tuple) else [name]
    for s in args:
        if s in (list, tuple):
            ans.extend(s)
        else:
            ans.append(s)
    final = f"Hello, {ans[0]}"
    for i in range(1, len(ans)):
        final += f' and {ans[i]}'
    final += '!'
    return final

        