def sq_sum(*args):
    ans = 0
    for i in range(len(args)):
        ans += args[i] ** 2
    return(ans) 